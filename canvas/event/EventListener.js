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
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} listener
     * @param {boolean} useCapture
     * @returns
     */
    constructor (type, listener, useCapture) {

        this.type = type;
        this.listener = listener;
        this.useCapture = useCapture;

    }


}
