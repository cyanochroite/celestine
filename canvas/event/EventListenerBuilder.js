import {EventListener} from "./EventListener";
import {EventType} from "./EventType";

/**
 * @class
 */
export class EventListenerBuilder {


    /**
     * @param {(argument: Event | EventTarget) => void} method
     * @returns {(event: Event) => void}
     */
    static listenerUseEvent (method) {


        return (event) => method(event);

    }


    /**
     * @param {(argument: Event | EventTarget) => void} method
     * @returns {(event: Event) => void}
     */
    static listenerUseTarget (method) {

        return (event) => method(event.currentTarget);

    }


    /**
     * @param {(argument: Event | EventTarget) => void} method
     * @param {string} [type]
     * @returns {EventListener}
     */
    static makeUsingEventAndBubble (method, type) {

        const
            listener = EventListenerBuilder.listenerUseEvent(method),
            useCapture = EventListenerBuilder.propagationUseBubble();
        return new EventListener(type, listener, useCapture);

    }


    /**
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} method
     * @returns {EventListener}
     */
    static makeUsingEventAndCapture (type, method) {

        const
            listener = EventListenerBuilder.listenerUseEvent(method),
            useCapture = EventListenerBuilder.propagationUseCapture();
        return new EventListener(type, listener, useCapture);

    }


    /**
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} method
     * @returns {EventListener}
     */
    static makeUsingTargetAndBubble (type, method) {

        const
            listener = EventListenerBuilder.listenerUseTarget(method),
            useCapture = EventListenerBuilder.propagationUseBubble();
        return new EventListener(type, listener, useCapture);

    }


    /**
     * @param {string} type
     * @param {(argument: Event | EventTarget) => void} method
     * @returns {EventListener}
     */
    static makeUsingTargetAndCapture (type, method) {

        const
            listener = EventListenerBuilder.listenerUseTarget(method),
            useCapture = EventListenerBuilder.propagationUseCapture();
        return new EventListener(type, listener, useCapture);

    }

    /**
     * @returns {boolean}
     */
    static propagationUseBubble () {

        return false;

    }


    /**
     * @returns {boolean}
     */
    static propagationUseCapture () {

        return true;

    }


    static demo () {

        const arg = EventType.Event.fail;
        EventListenerBuilder.makeUsingEventAndBubble(arg);

    }


}


