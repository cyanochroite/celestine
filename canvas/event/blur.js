/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*global
    document, add_event, add_event_blur, add_event_blur_all_now, add_event_blur_all_run,
    add_event_blur_one_now, add_event_blur_one_run, add_event_change, add_event_change_all_now,
    add_event_change_all_run, add_event_change_one_now, add_event_change_one_run,
    add_event_click, add_event_click_all_now, add_event_click_all_run, add_event_click_one_now,
    add_event_click_one_run, add_event_keydown, add_event_keydown_all_now,
    add_event_keydown_all_run, add_event_keydown_one_now, add_event_keydown_one_run,
    add_event_null, add_event_null_all_now, add_event_null_all_run, add_event_null_one_now,
    add_event_null_one_run
*/
/*property
    addEventListener, classList, contains, currentTarget, key, length,
    querySelector, querySelectorAll
*/
/* add_event_blur */
/**
 * @param {boolean} do_all
 * @param {boolean} do_now
 * @param {any} selector
 * @param {(arg0: any) => void} method
 */
function add_event_blur(do_all, do_now, selector, method) {
    "use strict";
    var event_listener = listener_event_make("blur", method, false, true);
    var selected = listener_selector(do_all, selector);
    listener_add(event_listener, selected, do_now, method);
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