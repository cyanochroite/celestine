/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*property
    addEventListener, classList, contains, currentTarget, key, length,
    querySelector, querySelectorAll
*/


/**
 * @param {HTMLElement} element
 * @param {{
 *   type: string;
 *   listener: (name: any) => void;
 *   use_capture: boolean;
 * }} event
**/
function add_event_listener(element, event) {
    var type = event.type;
    var listener = event.listener;
    var use_capture = event.use_capture;
    element.addEventListener(type, listener, use_capture);
}
var car = document.querySelectorAll('fish');
var pig = {
    type: "4", listener: function (add_event) {
        alert(add_event.currentTarget);
    }, use_capture: false
}
add_event_listener(car, pig)
function action(event_listener, select_all, call_immediately, selector, method) {
    "use strict";
    event_listener = {};
    event_listener.type = "blur";
    event_listener.listener = "blur";
    event_listener.use_capture = false;
    var item;
    var element = (
        select_all
            ? document.querySelectorAll(selector)
            : [document.querySelector(selector)]
    );
    var index = element.length;
    while (index) {
        index -= 1;
        item = element[index];
        if (item && !item.classList.contains("disabled")) {
            if (call_immediately) {
                method(element[index]);
            }
            if (event_listener) {
                add_event_listener(element[index], event_listener);
            }
        }
    }
}
function action(type, listener, select_all, call_immediately, selector, method) {
    "use strict";
    var item;
    var element = (
        select_all
            ? document.querySelectorAll(selector)
            : [document.querySelector(selector)]
    );
    var index = element.length;
    while (index) {
        index -= 1;
        item = element[index];
        if (item && !item.classList.contains("disabled")) {
            if (call_immediately) {
                method(element[index]);
            }
            if (type) {
                element[index].addEventListener(type, listener, false);
            }
        }
    }
}
function action(name, do_all, do_now, selector, method, callback) {
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
/* add_event_blur */
/**
 * @param {boolean} do_all
 * @param {boolean} do_now
 * @param {any} selector
 * @param {(arg0: any) => void} method
 */
function add_event_blur(do_all, do_now, selector, method) {
    "use strict";
    add_event("blur", do_all, do_now, selector, method, /**
         * @param {{ currentTarget: any; }} add_event
         */
        function (add_event) {
            method(add_event.currentTarget);
        });
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_blur_all_now(selector, method) {
    "use strict";
    add_event_blur(true, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_blur_all_run(selector, method) {
    "use strict";
    add_event_blur(true, false, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_blur_one_now(selector, method) {
    "use strict";
    add_event_blur(false, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_blur_one_run(selector, method) {
    "use strict";
    add_event_blur(false, false, selector, method);
}
/* add_event_change */
/**
 * @param {boolean} do_all
 * @param {boolean} do_now
 * @param {any} selector
 * @param {(arg0: any) => void} method
 */
function add_event_change(do_all, do_now, selector, method) {
    "use strict";
    add_event("change", do_all, do_now, selector, method, /**
         * @param {{ currentTarget: any; }} add_event
         */
        function (add_event) {
            method(add_event.currentTarget);
        });
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_change_all_now(selector, method) {
    "use strict";
    add_event_change(true, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_change_all_run(selector, method) {
    "use strict";
    add_event_change(true, false, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_change_one_now(selector, method) {
    "use strict";
    add_event_change(false, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_change_one_run(selector, method) {
    "use strict";
    add_event_change(false, false, selector, method);
}
/* add_event_click */
/**
 * @param {boolean} do_all
 * @param {boolean} do_now
 * @param {any} selector
 * @param {(arg0: any) => void} method
 */
function add_event_click(do_all, do_now, selector, method) {
    "use strict";
    add_event("click", do_all, do_now, selector, method, /**
         * @param {{ currentTarget: any; }} add_event
         */
        function (add_event) {
            method(add_event.currentTarget);
        });
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_click_all_now(selector, method) {
    "use strict";
    add_event_click(true, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_click_all_run(selector, method) {
    "use strict";
    add_event_click(true, false, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_click_one_now(selector, method) {
    "use strict";
    add_event_click(false, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_click_one_run(selector, method) {
    "use strict";
    add_event_click(false, false, selector, method);
}
/* add_event_keydown */
/**
 * @param {boolean} do_all
 * @param {boolean} do_now
 * @param {any} selector
 * @param {(arg0: any, arg1: any) => void} method
 */
function add_event_keydown(do_all, do_now, selector, method) {
    "use strict";
    add_event("keydown", do_all, do_now, selector, method, /**
         * @param {{ currentTarget: any; key: any; }} add_event
         */
        function (add_event) {
            method(add_event.currentTarget, add_event.key);
        });
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_keydown_all_now(selector, method) {
    "use strict";
    add_event_keydown(true, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_keydown_all_run(selector, method) {
    "use strict";
    add_event_keydown(true, false, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_keydown_one_now(selector, method) {
    "use strict";
    add_event_keydown(false, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_keydown_one_run(selector, method) {
    "use strict";
    add_event_keydown(false, false, selector, method);
}
/* add_event_null */
/**
 * @param {boolean} do_all
 * @param {boolean} do_now
 * @param {any} selector
 * @param {(arg0: any) => void} method
 */
function add_event_null(do_all, do_now, selector, method) {
    "use strict";
    add_event(null, do_all, do_now, selector, method, /**
         * @param {{ currentTarget: any; }} add_event
         */
        function (add_event) {
            method(add_event.currentTarget);
        });
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_null_all_now(selector, method) {
    "use strict";
    add_event_null(true, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_null_all_run(selector, method) {
    "use strict";
    add_event_null(true, false, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_null_one_now(selector, method) {
    "use strict";
    add_event_null(false, true, selector, method);
}
/**
 * @param {any} selector
 * @param {any} method
 */
function add_event_null_one_run(selector, method) {
    "use strict";
    add_event_null(false, false, selector, method);
}