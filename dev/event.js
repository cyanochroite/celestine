/* JSLint edition 2019-01-31 */
/*jslint
    browser:true
*/
/*global
    document, event, event_blur, event_blur_all_now, event_blur_all_run,
    event_blur_one_now, event_blur_one_run, event_change, event_change_all_now,
    event_change_all_run, event_change_one_now, event_change_one_run,
    event_click, event_click_all_now, event_click_all_run, event_click_one_now,
    event_click_one_run, event_focus, event_focus_all_now, event_focus_all_run,
    event_focus_one_now, event_focus_one_run, event_keydown,
    event_keydown_all_now, event_keydown_all_run, event_keydown_one_now,
    event_keydown_one_run, event_load, event_load_all_now, event_load_all_run,
    event_load_one_now, event_load_one_run, event_null, event_null_all_now,
    event_null_all_run, event_null_one_now, event_null_one_run, event_submit,
    event_submit_all_now, event_submit_all_run, event_submit_one_now,
    event_submit_one_run
*/
/*property
    addEventListener, classList, contains, currentTarget, key, length,
    querySelector, querySelectorAll
*/
function event(name, do_all, do_now, selector, method, callback) {
    "use strict";
    var item;
    var element = (
        do_all
        ? document.querySelectorAll(selector)
        : [document.querySelector(selector)]
    );
    var index = element.length;
    while (index) {
        index -= 1;
        item = element[index];
        if (item && !item.classList.contains("disabled")) {
            if (do_now) {
                method(element[index]);
            }
            if (name) {
                element[index].addEventListener(name, callback);
            }
        }
    }
}
/* event_blur */
function event_blur(do_all, do_now, selector, method) {
    "use strict";
    event("blur", do_all, do_now, selector, method, function (event) {
        method(event.currentTarget);
    });
}
function event_blur_all_now(selector, method) {
    "use strict";
    event_blur(true, true, selector, method);
}
function event_blur_all_run(selector, method) {
    "use strict";
    event_blur(true, false, selector, method);
}
function event_blur_one_now(selector, method) {
    "use strict";
    event_blur(false, true, selector, method);
}
function event_blur_one_run(selector, method) {
    "use strict";
    event_blur(false, false, selector, method);
}
/* event_change */
function event_change(do_all, do_now, selector, method) {
    "use strict";
    event("change", do_all, do_now, selector, method, function (event) {
        method(event.currentTarget);
    });
}
function event_change_all_now(selector, method) {
    "use strict";
    event_change(true, true, selector, method);
}
function event_change_all_run(selector, method) {
    "use strict";
    event_change(true, false, selector, method);
}
function event_change_one_now(selector, method) {
    "use strict";
    event_change(false, true, selector, method);
}
function event_change_one_run(selector, method) {
    "use strict";
    event_change(false, false, selector, method);
}
/* event_click */
function event_click(do_all, do_now, selector, method) {
    "use strict";
    event("click", do_all, do_now, selector, method, function (event) {
        method(event.currentTarget);
    });
}
function event_click_all_now(selector, method) {
    "use strict";
    event_click(true, true, selector, method);
}
function event_click_all_run(selector, method) {
    "use strict";
    event_click(true, false, selector, method);
}
function event_click_one_now(selector, method) {
    "use strict";
    event_click(false, true, selector, method);
}
function event_click_one_run(selector, method) {
    "use strict";
    event_click(false, false, selector, method);
}
/* event_focus */
function event_focus(do_all, do_now, selector, method) {
    "use strict";
    event("focus", do_all, do_now, selector, method, function (event) {
        method(event.currentTarget);
    });
}
function event_focus_all_now(selector, method) {
    "use strict";
    event_focus(true, true, selector, method);
}
function event_focus_all_run(selector, method) {
    "use strict";
    event_focus(true, false, selector, method);
}
function event_focus_one_now(selector, method) {
    "use strict";
    event_focus(false, true, selector, method);
}
function event_focus_one_run(selector, method) {
    "use strict";
    event_focus(false, false, selector, method);
}
/* load */
function event_load(do_all, do_now, selector, method) {
    "use strict";
    event("load", do_all, do_now, selector, method, function (event) {
        method(event.currentTarget);
    });
}
function event_load_all_now(selector, method) {
    "use strict";
    event_load(true, true, selector, method);
}
function event_load_all_run(selector, method) {
    "use strict";
    event_load(true, false, selector, method);
}
function event_load_one_now(selector, method) {
    "use strict";
    event_load(false, true, selector, method);
}
function event_load_one_run(selector, method) {
    "use strict";
    event_load(false, false, selector, method);
}
/* submit */
function event_submit(do_all, do_now, selector, method) {
    "use strict";
    event("submit", do_all, do_now, selector, method, function (event) {
        method(event.currentTarget);
    });
}
function event_submit_all_now(selector, method) {
    "use strict";
    event_submit(true, true, selector, method);
}
function event_submit_all_run(selector, method) {
    "use strict";
    event_submit(true, false, selector, method);
}
function event_submit_one_now(selector, method) {
    "use strict";
    event_submit(false, true, selector, method);
}
function event_submit_one_run(selector, method) {
    "use strict";
    event_submit(false, false, selector, method);
}
/* event_keydown */
function event_keydown(do_all, do_now, selector, method) {
    "use strict";
    event("keydown", do_all, do_now, selector, method, function (event) {
        method(event.currentTarget, event.key);
    });
}
function event_keydown_all_now(selector, method) {
    "use strict";
    event_keydown(true, true, selector, method);
}
function event_keydown_all_run(selector, method) {
    "use strict";
    event_keydown(true, false, selector, method);
}
function event_keydown_one_now(selector, method) {
    "use strict";
    event_keydown(false, true, selector, method);
}
function event_keydown_one_run(selector, method) {
    "use strict";
    event_keydown(false, false, selector, method);
}
/* event_null */
function event_null(do_all, do_now, selector, method) {
    "use strict";
    event(null, do_all, do_now, selector, method, function (event) {
        method(event.currentTarget);
    });
}
function event_null_all_now(selector, method) {
    "use strict";
    event_null(true, true, selector, method);
}
function event_null_all_run(selector, method) {
    "use strict";
    event_null(true, false, selector, method);
}
function event_null_one_now(selector, method) {
    "use strict";
    event_null(false, true, selector, method);
}
function event_null_one_run(selector, method) {
    "use strict";
    event_null(false, false, selector, method);
}