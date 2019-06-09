function event__add (selected, event_listener) {

    "use strict";

    let {listener} = event_listener,
     {type} = event_listener,
     {use_capture} = event_listener;

    selected.forEach((element) => {
        element.addEventListener(type, listener, use_capture);
    });

}

/**
 * @param {Element[]} selected
 * @param {(element: Element) => void} method
 * @returns {void}
 */
function event__run (selected, method) {

    selected.forEach((element) => {
        method(element);
    });

}

/**
 * @param {string} selector
 * @returns {Element[]} selected
 */
function event__select_all (selector) {

    let array = [];

    
return array.slice.call(document.querySelectorAll(selector));

}

/**
 * @param {string} selector
 * @returns {Element[]} selected
 */
function event__select_one (selector) {

    return [document.querySelector(selector)];

}


function event__listener_make () {

    let event_listener = {};

    event_listener.type = "";

    /**
     * @param {Event} event
     */
    event_listener.listener = (event) => event;
    event_listener.use_capture = false;
    
return event_listener;

}

/**
 * @param {string} type
 * @param {{ type: string; }} event_listener
 */
function event__listener_type (event_listener, type) {

    event_listener.type = type;

}

/**
 * @param {{ use_capture: boolean; }} event_listener
 */
function event__listener_use_bubble (event_listener) {

    event_listener.use_capture = false;

}

/**
 * @param {{ use_capture: boolean; }} event_listener
 */
function event__listener_use_capture (event_listener) {

    event_listener.use_capture = false;

}

/**
 * @param {{ listener: (event: Event) => void; }} event_listener
 * @param {(argument: Event) => void} method
 */
function event__listener_use_event (event_listener, method) {


    /**
     * @param {Event} event
     */
    event_listener.listener = (event) => method(event);

}

/**
 * @param {{ listener: (event: Event) => void; }} event_listener
 * @param {(argument: EventTarget) => void} method
 */
function event__listener_use_target (event_listener, method) {


    /**
     * @param {Event} event
     */
    event_listener.listener = (event) => method(event.currentTarget);

}


class listener {

    constructor () {

        this._type = "";

        /**
         * @param {Event} event
         */
        // This._listener = (event) => (event);
        this._use_capture = false;
    
}


    /**
     * @param {string} type
     */
    type (type) {

        this._type = type;
    
}

    use_bubble () {

        this._use_capture = false;
    
}

    use_capture () {

        this._use_capture = true;
    
}


    /**
     * @param {(argument: Event) => void} method
     */
    use_event (method) {


        /**
         * @param {Event} event
         */
        this._listener = (event) => method(event);
    
}

    /**
     * @param {(argument: EventTarget) => void} method
     */
    use_target (method) {


        /**
         * @param {Event} event
         */
        this._listener = (event) => method(event.currentTarget);
    
}

}
