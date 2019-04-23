/*jslint
    browser:true
*/
/*global
    document, event_blur, event_change, event_click, event_focus, event_load,
    event_run, event_submit
*/
/*property
    addEventListener, classList, contains, currentTarget, length,
    querySelector, querySelectorAll
*/
function event_run(do_now, do_all, selectors, method, type) {
    "use strict";
    var callback = function (item) {
        method(item.currentTarget);
    };
    var element = do_all
        ? document.querySelectorAll(selectors)
        : [document.querySelector(selectors)];
    var index = element.length;
    while (index) {
        index -= 1;
        if (element[index] && !element[index].classList.contains("disabled")) {
            if (do_now) {
                method(element[index]);
            }
            if (type) {
                element[index].addEventListener(type, callback);
            }
        }
    }
}
function event_blur(do_now, do_all, selectors, method) {
    "use strict";
    event_run(do_now, do_all, selectors, method, "blur");
}
function event_change(do_now, do_all, selectors, method) {
    "use strict";
    event_run(do_now, do_all, selectors, method, "change");
}
function event_click(do_now, do_all, selectors, method) {
    "use strict";
    event_run(do_now, do_all, selectors, method, "click");
}
function event_focus(do_now, do_all, selectors, method) {
    "use strict";
    event_run(do_now, do_all, selectors, method, "focus");
}
function event_load(do_now, do_all, selectors, method) {
    "use strict";
    event_run(do_now, do_all, selectors, method, "load");
}
function event_submit(do_now, do_all, selectors, method) {
    "use strict";
}