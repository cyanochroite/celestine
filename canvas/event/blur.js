/**
 * @class
 */
// eslint-disable-next-line no-unused-vars
class eventBlur {

}

/**
 * @param {Element[]} selected
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur (selected, method) {

    "use strict";
    let event_listener = event__listener_make();
    event__listener_type(event_listener, "blur");
    event__listener_use_bubble(event_listener);
    event__listener_use_target(event_listener, method);
    event__add(selected, event_listener);

}

/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur_all_now (selector, method) {

    let selected = event__select_all(selector);
    event__blur(selected, method);
    event__run(selected, method);

}

/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur_all_run (selector, method) {

    let selected = event__select_all(selector);
    event__blur(selected, method);

}

/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur_one_now (selector, method) {

    let selected = event__select_one(selector);
    event__blur(selected, method);
    event__run(selected, method);

}

/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur_one_run (selector, method) {

    let selected = event__select_one(selector);
    event__blur(selected, method);

}
