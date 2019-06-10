/**
 * @class
 */
export class listener {


    /**
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} [method]
     * @param {boolean} [useCapture]
     * @returns
     */
    constructor (type, method, useCapture) {

        this.type = type;

        /**
         * @param {Event} event
         * @returns {void}
         */
        this.listener = (event) => method(event);
        this.useCapture = useCapture;

    }


    /**
     * @param {(argument: Event) => void} method
     * @returns {void}
     */
    listenerUseEvent (method) {


        /**
         * @param {Event} event
         * @returns {void}
         */
        this.listener = (event) => method(event);

    }


    /**
     * @param {(argument: EventTarget) => void} method
     * @returns {void}
     */
    listenerUseTarget (method) {


        /**
         * @param {Event} event
         * @returns {void}
         */
        this.listener = (event) => method(event.currentTarget);

    }


    /**
     * @returns {void}
     */
    propagationUseBubble () {

        this.useCapture = false;

    }


    /**
     * @returns {void}
     */
    propagationUseCapture () {

        this.useCapture = true;

    }

}
