import sys
import os
import textwrap

from coverage import env
from coverage.collector import CTracer
import coverage




OK = 0
ERR = 1
FAIL_UNDER = 2


HELP_TOPICS = {
    'help': """\
        Coverage.py, version {__version__} {extension_modifier}
        Measure, collect, and report on code coverage in Python programs.

        usage: {program_name} <command> [options] [args]

        Commands:
            annotate    Annotate source files with execution information.
            combine     Combine a number of data files.
            debug       Display information about the internals of coverage.py
            erase       Erase previously collected coverage data.
            help        Get help on using coverage.py.
            html        Create an HTML report.
            json        Create a JSON report of coverage results.
            lcov        Create an LCOV report of coverage results.
            report      Report coverage stats on modules.
            run         Run a Python program and measure code execution.
            xml         Create an XML report of coverage results.

        Use "{program_name} help <command>" for detailed help on any command.
    """,

    'minimum_help': """\
        Code coverage for Python, version {__version__} {extension_modifier}.  Use '{program_name} help' for help.
    """,

    'version': """\
        Coverage.py, version {__version__} {extension_modifier}
    """,
}


def show_help(error=None, topic=None, parser=None):
    """Display an error message, or the named topic."""
    assert error or topic or parser

    program_path = sys.argv[0]
    if program_path.endswith(os.path.sep + '__main__.py'):
        # The path is the main module of a package; get that path instead.
        program_path = os.path.dirname(program_path)
    program_name = os.path.basename(program_path)
    if env.WINDOWS:
        # entry_points={'console_scripts':...} on Windows makes files
        # called coverage.exe, coverage3.exe, and coverage-3.5.exe. These
        # invoke coverage-script.py, coverage3-script.py, and
        # coverage-3.5-script.py.  argv[0] is the .py file, but we want to
        # get back to the original form.
        auto_suffix = "-script.py"
        if program_name.endswith(auto_suffix):
            program_name = program_name[:-len(auto_suffix)]

    help_params = dict(coverage.__dict__)
    help_params['program_name'] = program_name
    if CTracer is not None:
        help_params['extension_modifier'] = 'with C extension'
    else:
        help_params['extension_modifier'] = 'without C extension'

    if error:
        print(error, file=sys.stderr)
        print(f"Use '{program_name} help' for help.", file=sys.stderr)
    elif parser:
        print(parser.format_help().strip())
        print()
    else:
        help_msg = textwrap.dedent(HELP_TOPICS.get(topic, '')).strip()
        if help_msg:
            print(help_msg.format(**help_params))
        else:
            print(f"Don't know topic {topic!r}")
    print("Full documentation is at {__url__}".format(**help_params))

    
def command_line(self, argv):
    """The bulk of the command line interface to coverage.py.

    `argv` is the argument list to process.

    Returns 0 if all is well, 1 if something went wrong.

    """
    # Collect the command-line options.
    if not argv:
        show_help(topic='minimum_help')
        return OK

    # The command syntax we parse depends on the first argument.  Global
    # switch syntax always starts with an option.
    self.global_option = argv[0].startswith('-')
    if self.global_option:
        parser = GlobalOptionParser()
    else:
        parser = COMMANDS.get(argv[0])
        if not parser:
            show_help(f"Unknown command: {argv[0]!r}")
            return ERR
        argv = argv[1:]

    ok, options, args = parser.parse_args_ok(argv)
    if not ok:
        return ERR

    # Handle help and version.
    if self.do_help(options, args, parser):
        return OK

    # Listify the list options.
    source = unshell_list(options.source)
    omit = unshell_list(options.omit)
    include = unshell_list(options.include)
    debug = unshell_list(options.debug)
    contexts = unshell_list(options.contexts)

    if options.concurrency is not None:
        concurrency = options.concurrency.split(",")
    else:
        concurrency = None

    # Do something.
    self.coverage = Coverage(
        data_file=options.data_file or DEFAULT_DATAFILE,
        data_suffix=options.parallel_mode,
        cover_pylib=options.pylib,
        timid=options.timid,
        branch=options.branch,
        config_file=options.rcfile,
        source=source,
        omit=omit,
        include=include,
        debug=debug,
        concurrency=concurrency,
        check_preimported=True,
        context=options.context,
        messages=not options.quiet,
        )

    if options.action == "debug":
        return self.do_debug(args)

    elif options.action == "erase":
        self.coverage.erase()
        return OK

    elif options.action == "run":
        return self.do_run(options, args)

    elif options.action == "combine":
        if options.append:
            self.coverage.load()
        data_paths = args or None
        self.coverage.combine(data_paths, strict=True, keep=bool(options.keep))
        self.coverage.save()
        return OK

    # Remaining actions are reporting, with some common options.
    report_args = dict(
        morfs=unglob_args(args),
        ignore_errors=options.ignore_errors,
        omit=omit,
        include=include,
        contexts=contexts,
        )

    # We need to be able to import from the current directory, because
    # plugins may try to, for example, to read Django settings.
    sys.path.insert(0, '')

    self.coverage.load()

    total = None
    if options.action == "report":
        total = self.coverage.report(
            precision=options.precision,
            show_missing=options.show_missing,
            skip_covered=options.skip_covered,
            skip_empty=options.skip_empty,
            sort=options.sort,
            **report_args
            )
    elif options.action == "annotate":
        self.coverage.annotate(directory=options.directory, **report_args)
    elif options.action == "html":
        total = self.coverage.html_report(
            directory=options.directory,
            precision=options.precision,
            skip_covered=options.skip_covered,
            skip_empty=options.skip_empty,
            show_contexts=options.show_contexts,
            title=options.title,
            **report_args
            )
    elif options.action == "xml":
        total = self.coverage.xml_report(
            outfile=options.outfile,
            skip_empty=options.skip_empty,
            **report_args
            )
    elif options.action == "json":
        total = self.coverage.json_report(
            outfile=options.outfile,
            pretty_print=options.pretty_print,
            show_contexts=options.show_contexts,
            **report_args
            )
    elif options.action == "lcov":
        total = self.coverage.lcov_report(
            outfile=options.outfile,
            **report_args
            )
    else:
        # There are no other possible actions.
        raise AssertionError

    if total is not None:
        # Apply the command line fail-under options, and then use the config
        # value, so we can get fail_under from the config file.
        if options.fail_under is not None:
            self.coverage.set_option("report:fail_under", options.fail_under)
        if options.precision is not None:
            self.coverage.set_option("report:precision", options.precision)

        fail_under = self.coverage.get_option("report:fail_under")
        precision = self.coverage.get_option("report:precision")
        if should_fail_under(total, fail_under, precision):
            msg = "total of {total} is less than fail-under={fail_under:.{p}f}".format(
                total=Numbers(precision=precision).display_covered(total),
                fail_under=fail_under,
                p=precision,
            )
            print("Coverage failure:", msg)
            return FAIL_UNDER

    return OK

def main():
    command_line(None, None)
    return OK

if __name__ == "__main__":
    sys.exit(main())

