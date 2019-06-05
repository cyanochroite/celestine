/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*global
    document, element_select_all, element_select_one, event_add,
    event_add_listener, event_run, listener_for_current_event,
    listener_for_current_target, make_event_listener
*/
/*property
    addEventListener, call, currentTarget, length, listener, querySelector,
    querySelectorAll, slice, type, use_capture
*/
/**
 * @param {(event: Event) => void} method
**/
function listener_for_current_event(method) {
    var listener =
        /**
         * @param {Event} event
        **/
        (event) => method(event);
    return listener;
}
/**
 * @param {(target: EventTarget) => void} method
**/
function listener_for_current_target(method) {
    var listener =
        /**
         * @param {Event} event
        **/
        (event) => method(event.currentTarget);
    return listener;
}
/**
 * @param {string} type
 * @param {boolean} use_capture
 * @param {(event: Event | EventTarget) => void} method
 * @param {boolean} use_current_target
**/
function make_event_listener(type, method, use_capture, use_current_target) {
    var listener;
    if (use_current_target) {
        listener = listener_for_current_target(method);
    } else {
        listener = listener_for_current_event(method);
    }
    var event_listener = {};
    event_listener.type = type;
    event_listener.listener = listener;
    event_listener.use_capture = use_capture;
    return event_listener;
}


/**
 * @param {string} selector
 * @returns {Element[]} selected
**/
function element_select_one(selector) {
    return [document.querySelector(selector)];
}
/**
 * @param {string} selector
 * @returns {Element[]} selected
**/
function element_select_all(selector) {
    var array = [];
    return array.slice.call(document.querySelectorAll(selector));
}
/**
 * @param {Element[]} selected
 * @param {(element: Element) => void} method
 * @returns {void}
 */
function event_run(selected, method) {
    var index = selected.length;
    while (index > 0) {
        index -= 1;
        method(selected[index]);
    }
}
/**
 * @param {Element} element
 * @param {{
 *   type: string;
 *   listener: any;
 *   use_capture: boolean;
 * }} event_listener
**/
function event_add_listener(element, event_listener) {
    var type = event_listener.type;
    var listener = event_listener.listener;
    var use_capture = event_listener.use_capture;
    element.addEventListener(type, listener, use_capture);
}
/**
 * @param {Element[]} selected
 * @param {{
 *   type: string;
 *   listener: any;
 *   use_capture: boolean;
 * }} event_listener
**/
function event_add(selected, event_listener) {
    var index = selected.length;
    while (index > 0) {
        index -= 1;
        event_add_listener(selected[index], event_listener);
    }
}