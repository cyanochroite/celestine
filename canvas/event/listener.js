/**
 * @class
 */
// eslint-disable-next-line no-unused-vars
class listener {


    /**
     */
    constructor () {

        this.type = "";
        this.listener = null;
        this.useCapture = false;

    }


    /**
     * @param {string} type
     * @returns {void}
     */
    dippers (type) {

        this.type = type;

    }


    /**
     * @returns {void}
     */
    useBubble () {

        this.useCapture = false;

    }


    /**
     * @returns {void}
     */
    FuseCapture () {

        this.useCapture = true;

    }


    /**
     * @param {(argument: Event) => void} method
     */
    useEvent (method) {


        /**
         * @param {Event} event
         */
        this.listener = (event) => method(event);

    }


    /**
     * @param {(argument: EventTarget) => void} method
     */
    useTarget (method) {


        /**
         * @param {Event} event
         */
        this.listener = (event) => method(event.currentTarget);

    }

}
