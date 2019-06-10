/**
 * @class
 */
export class EventListener {


    /**
     * @param {Element} element
     */
    applyToElement (element) {

        element.addEventListener(
            this.type,
            this.listener,
            this.useCapture
        );

    }

    /**
     * @param {(argument: Event | EventTarget) => void} [method]
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
     * @param {(argument: Event | EventTarget) => void} [method]
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
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} [method]
     * @returns {EventListener}
     */
    static makeUsingEventAndBubble (type, method) {

        const eventListener = new EventListener(type);
        eventListener.listenerUseEvent(method);
        eventListener.propagationUseBubble();
        return eventListener;

    }


    /**
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} [method]
     * @returns {EventListener}
     */
    static makeUsingEventAndCapture (type, method) {

        const eventListener = new EventListener(type);
        eventListener.listenerUseEvent(method);
        eventListener.propagationUseCapture();
        return eventListener;

    }


    /**
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} [method]
     * @returns {EventListener}
     */
    static makeUsingTargetAndBubble (type, method) {

        const eventListener = new EventListener(type);
        eventListener.listenerUseTarget(method);
        eventListener.propagationUseBubble();
        return eventListener;

    }


    /**
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} [method]
     * @returns {EventListener}
     */
    static makeUsingTargetAndCapture (type, method) {

        const eventListener = new EventListener(type);
        eventListener.listenerUseTarget(method);
        eventListener.propagationUseCapture();
        return eventListener;

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


}
