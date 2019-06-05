/*
    JSLint edition 2019-01-31
*/
/*jslint
    browser:true
*/
/*global
    add_event_listener, document, listener, query_selector
*/
/*property
    addEventListener, length, listener, querySelector, querySelectorAll, type,
    use_capture
*/
/**
 * @param {Element} element
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
/**
 * @param {boolean} select_all
 * @param {string} selector
**/
function query_selector(select_all, selector) {
    var element;
    if (select_all) {
        element = document.querySelectorAll(selector);
    } else {
        element = [document.querySelector(selector)];
    }
    return element;
}

/**
 * @param {{
 *    currentTarget: any;
 * }} add_event
 * @param {(arg0: any) => void} method
**/
function callback(method, add_event) {
    method(add_event.currentTarget);
}

/**
 * @param {{
 *   type: string;
 *   listener: (name: any) => void;
 *   use_capture: boolean;
 * }} event
 * @param {any} select_all
 * @param {any} call_immediately
 * @param {any} selector
 * @param {(arg0: any) => void} method
**/
function listener(event, select_all, call_immediately, selector, method) {
    "use strict";
    var element = query_selector(select_all, selector);
    var index = element.length;
    while (index) {
        index -= 1;
        if (call_immediately) {
            method(element[index]);
        }
        if (event) {
            add_event_listener(element[index], event);
        }
    }
}