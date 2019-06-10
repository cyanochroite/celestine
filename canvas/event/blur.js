import {listener} from "./listener";

/**
 * @class
 */
export class eventBlur extends listener {


    /**
     */
    constructor () {

        super();
        this.type = "";
        this.listener = null;
        this.useCapture = false;

    }


    /**
     * @param {Element[]} selected
     * @param {(event: Event | EventTarget) => void} method
     */
    blur (selected, method) {


        const event_listener = event__listener_make();
        event__listener_type(event_listener, "blur");
        event__listener_use_bubble(event_listener);
        event__listener_use_target(event_listener, method);
        event__add(selected, event_listener);

    }

    /**
     * @param {string} selector
     * @param {(event: Event | EventTarget) => void} method
     */
    all_now (selector, method) {

        const selected = event__select_all(selector);
        event__blur(selected, method);
        event__run(selected, method);

    }

    /**
     * @param {string} selector
     * @param {(event: Event | EventTarget) => void} method
     */
    all_run (selector, method) {

        const selected = event__select_all(selector);
        event__blur(selected, method);

    }

    /**
     * @param {string} selector
     * @param {(event: Event | EventTarget) => void} method
     */
    one_now (selector, method) {

        const selected = event__select_one(selector);
        event__blur(selected, method);
        event__run(selected, method);

    }

    /**
     * @param {string} selector
     * @param {(event: Event | EventTarget) => void} method
     */
    one_run (selector, method) {

        const selected = event__select_one(selector);
        event__blur(selected, method);

    }


}
