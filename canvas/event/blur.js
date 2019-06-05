/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*global
    element_select_all, element_select_one, event_add, event_blur,
    event_blur_all_now, event_blur_all_run, event_blur_one_now,
    event_blur_one_run, event_run, make_event_listener
*/
/*property
*/
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
 * @param {boolean} do_all
 * @param {boolean} do_now
**/
function event_blur(selector, method, do_all, do_now) {
    "use strict";
    var selected;
    var event_listener = make_event_listener("blur", method, false, true);
    if (do_all) {
        selected = element_select_all(selector);
    } else {
        selected = element_select_one(selector);
    }
    event_add(selected, event_listener);
    if (do_now) {
        event_run(selected, method);
    }
}
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
**/
function event_blur_all_now(selector, method) {
    event_blur(selector, method, true, true);
}
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
**/
function event_blur_all_run(selector, method) {
    event_blur(selector, method, true, false);
}
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
**/
function event_blur_one_now(selector, method) {
    event_blur(selector, method, false, true);
}
/**
 * @param {string} selector
 * @param {(event: Event | EventTarget) => void} method
**/
function event_blur_one_run(selector, method) {
    event_blur(selector, method, false, false);
}