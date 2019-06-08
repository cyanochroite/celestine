/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*global
    document, element_select_all, element_select_one, event__add,
    event__add_listener, event__run, make_event_listener
*/
/*property
    addEventListener, call, currentTarget, forEach, length, listener,
    querySelector, querySelectorAll, slice, type, use_capture
*/
/**
 * @param {Element[]} selected
 * @param {{
 *   type: string;
 *   listener: any;
 *   use_capture: boolean;
 * }} event_listener
 */
function event__add(selected, event_listener) {
    var listener = event_listener.listener;
    var type = event_listener.type;
    var use_capture = event_listener.use_capture;
    selected.forEach(function (element) {
        element.addEventListener(type, listener, use_capture);
    });
}
/**
 * @param {Element[]} selected
 * @param {(element: Element) => void} method
 * @returns {void}
 */
function event__run(selected, method) {
    selected.forEach(function (element) {
        method(element);
    });
}
/**
 * @param {string} selector
 * @returns {Element[]} selected
 */
function event__select_all(selector) {
    var array = [];
    return array.slice.call(document.querySelectorAll(selector));
}
/**
 * @param {string} selector
 * @returns {Element[]} selected
 */
function event__select_one(selector) {
    return [document.querySelector(selector)];
}
/**
 * @param {string} type
 * @param {(event: Event | EventTarget) => void} method
 * @param {boolean} use_capture
 * @param {boolean} use_target
 */
function event__make_event_listener(type, method, use_capture, use_target) {
    var listener;
    if (use_target) {
        /**
         * @param {Event} event
        **/
        listener = (event) => method(event.currentTarget);
    } else {
        /**
         * @param {Event} event
        **/
        listener = (event) => method(event);
    }
    var event_listener = {};
    event_listener.type = type;
    event_listener.listener = listener;
    event_listener.use_capture = use_capture;
    return event_listener;
}



/**
 * @param {{ use_capture: boolean; }} event_listener
 */
function event__listener_use_bubble(event_listener) {
    event_listener.use_capture = false;
}
/**
 * @param {{ use_capture: boolean; }} event_listener
 */
function event__listener_use_capture(event_listener) {
    event_listener.use_capture = false;
}
/**
 * @param {{ listener: (event: Event) => void; }} event_listener
 * @param {(argument: Event) => void} method
 */
function event__listener_use_event(event_listener, method) {
    /**
     * @param {Event} event
     */
    event_listener.listener = (event) => method(event);
}
/**
 * @param {{ listener: (event: Event) => void; }} event_listener
 * @param {(argument: EventTarget) => void} method
 */
function event__listener_use_target(event_listener, method) {
    /**
     * @param {Event} event
     */
    event_listener.listener = (event) => method(event.currentTarget);
}
