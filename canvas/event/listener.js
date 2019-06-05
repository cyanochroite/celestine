/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*global
    document, event, listener_add, listener_current_event,
    listener_current_target, listener_event_add, listener_event_make
*/
/*property
    addEventListener, currentTarget, length, listener, querySelector,
    querySelectorAll, type, use_capture
*/
/**
 * @param {(event: Event) => void} method
**/
function listener_current_event(method) {
    var listener =
        /**
         * @param {Event} event
        **/
        function (event) {
            method(event);
        };
    return listener;
}
/**
 * @param {(target: EventTarget) => void} method
**/
function listener_current_target(method) {
    var listener =
        /**
         * @param {Event} event
        **/
        function (event) {
            method(event.currentTarget);
        };
    return listener;
}
/**
 * @param {string} type
 * @param {boolean} use_capture
 * @param {(event: Event | EventTarget) => void} method
 * @param {boolean} use_current_target
**/
function listener_event_make(type, method, use_capture, use_current_target) {
    var listener;
    if (use_current_target) {
        listener = listener_current_target(method);
    }
    else {
        listener = listener_current_event(method);
    }
    var event_listener = {};
    event_listener.type = type;
    event_listener.listener = listener;
    event_listener.use_capture = use_capture;
    return event_listener;
}
/**
 * @param {Element} element
 * @param {{
 *   type: string;
 *   listener: any;
 *   use_capture: boolean;
 * }} event_listener
**/
function listener_event_add(element, event_listener) {
    var type = event_listener.type;
    var listener = event_listener.listener;
    var use_capture = event_listener.use_capture;
    element.addEventListener(type, listener, use_capture);
}
/**
 * @param {boolean} select_all
 * @param {string} selector
 */
function listener_selector(select_all, selector) {
    var element;
    if (select_all) {
        element = document.querySelectorAll(selector);
    } else {
        element = [document.querySelector(selector)];
    }
    return element;
}

/**
 * @param {boolean} call_immediately
 * @param {(arg0: Element) => void} [method]
 * @param {{ type: string; listener: any; use_capture: boolean; }} event_listener
 * @param {NodeListOf<Element> | Element[]} selected
 */
function listener_add(event_listener, selected, call_immediately, method) {
    "use strict";
    var index = selected.length;
    while (index) {
        index -= 1;
        if (call_immediately) {
            method(selected[index]);
        }
        if (event) {
            listener_event_add(selected[index], event_listener);
        }
    }
}
