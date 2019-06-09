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


function event__listener_make() {
    var event_listener = {};
    event_listener.type = "";
    /**
     * @param {Event} event
     */
    event_listener.listener = (event) => (event);
    event_listener.use_capture = false;
    return event_listener;
}
/**
 * @param {string} type
 * @param {{ type: string; }} event_listener
 */
function event__listener_type(event_listener, type) {
    event_listener.type = type;
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


class listener {
    constructor() {
        this._type = "";
        /**
         * @param {Event} event
         */
        //this._listener = (event) => (event);
        this._use_capture = false;
    }
    /**
     * @param {string} type
     */
    type(type) {
        this._type = type;
    }
    use_bubble() {
        this._use_capture = false;
    }
    use_capture() {
        this._use_capture = true;
    }
    /**
     * @param {(argument: Event) => void} method
     */
    use_event(method) {
        /**
         * @param {Event} event
         */
        this._listener = (event) => method(event);
    }

    /**
     * @param {(argument: EventTarget) => void} method
     */
    use_target(method) {
        /**
         * @param {Event} event
         */
        this._listener = (event) => method(event.currentTarget);
    }
}