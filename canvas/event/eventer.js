import {eventListener} from "./eventListener";

/**
 * @class
 */
// eslint-disable-next-line no-unused-vars
class eventer {


    /**
     * @param {Element[]} selected
     * @param {eventListener} listener
     */
    static add (selected, listener) {

        selected.forEach((element) => {

            listener.applyToElement(element);

        });

    }


    /**
     * @param {Element[]} selected
     * @param {(element: Element) => void} method
     * @returns {void}
     */
    static run (selected, method) {

        selected.forEach((element) => {

            method(element);

        });

    }


    /**
     * @param {string} selector
     * @returns {Element[]} selected
     */
    static selectAll (selector) {

        const array = [];
        return array.slice.call(document.querySelectorAll(selector));

    }


    /**
     * @param {string} selector
     * @returns {Element[]} selected
     */
    static selectOne (selector) {

        return [document.querySelector(selector)];

    }

}
