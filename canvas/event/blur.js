/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*global
    element_select_all, element_select_one, event__add, event__blur,
    event__blur_all_now, event__blur_all_run, event__blur_one_now,
    event__blur_one_run, event__run, make_event__listener
*/
/*property
*/
/**
 * @param {Element[]} selected
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur(selected, method) {
    "use strict";
    var event_listener = event__listener_make();
    event__listener_type(event_listener, "blur");
    event__listener_use_bubble(event_listener);
    event__listener_use_target(event_listener, method);
    event__add(selected, event_listener);
}
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur_all_now(selector, method) {
    var selected = event__select_all(selector);
    event__blur(selected, method);
    event__run(selected, method);
}
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur_all_run(selector, method) {
    var selected = event__select_all(selector);
    event__blur(selected, method);
}
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur_one_now(selector, method) {
    var selected = event__select_one(selector);
    event__blur(selected, method);
    event__run(selected, method);
}
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 */
function event__blur_one_run(selector, method) {
    var selected = event__select_one(selector);
    event__blur(selected, method);
}