/**
 * @class
 */
// eslint-disable-next-line no-unused-vars
class eventer extends listener {


    /**
     */
    constructor () {

        this.type = "";
        this.listener = null;
        this.useCapture = false;

    }


    /**
     * @param {Element[]} selected
     * @param {listener} eventListener
     */
    static add (selected, eventListener) {

        selected.forEach((element) => {

            element.addEventListener(
                eventListener.type,
                eventListener.listener,
                eventListener.useCapture
            );

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
