import {EventListener} from "./EventListener";

/**
 * @class
 */
export class EventBlur extends EventListener {


    /**
     */
    constructor () {

        super("blur");

    }


    /**
     * @param {(argument: Event | EventTarget) => void} method
     * @returns {EventListener}
     */
    static makeUsingEventAndBubble (method) {

        return super.makeUsingEventAndBubble(method);

    }

}
