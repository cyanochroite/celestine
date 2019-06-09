/**
 * @param {{ forEach: (arg0: (element: any) => void) => void; }} selected
 * @param {any} eventListener
 */
const eventAdd = function eventAdd (selected, eventListener) {

        "use strict";

        const {listener} = eventListener,
            {type} = eventListener,
            {useCapture} = eventListener;

        selected.forEach((element) => {

            element.addEventListener(type, listener, useCapture);

        });

        },

    /**
     * @param {Element[]} selected
     * @param {(element: Element) => void} method
     * @returns {void}
     */
    eventRun = function eventRun (selected, method) {

        selected.forEach((element) => {

            method(element);

        });

    };

/**
 * @param {string} selector
 * @returns {Element[]} selected
 */
function event__select_all (selector) {

    const array = [];


    return array.slice.call(document.querySelectorAll(selector));

}

/**
 * @param {string} selector
 * @returns {Element[]} selected
 */
function event__select_one (selector) {

    return [document.querySelector(selector)];

}
