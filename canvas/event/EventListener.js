/** @class */
export class EventListener {

    constructor (type) {

        this.type = type;
        this.callback = null;
        this.capture = null;

    }

    addEventListener (selected) {

        selected.forEach((element) => {

            element.addEventListener(this.type, this.callback, this.capture);

        });

    }

    SelectAllEventTargetBubblePhaseInvokeLater (selector, method) {

        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectAll(selector);
        this.addEventListener(selected);

    }

    SelectAllEventTargetBubblePhaseInvokeNow (selector, method) {

        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectAll(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);

    }

    SelectAllEventTargetCapturePhaseInvokeLater (selector, method) {

        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectAll(selector);
        this.addEventListener(selected);

    }

    SelectAllEventTargetCapturePhaseInvokeNow (selector, method) {

        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectAll(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);

    }

    SelectAllCurrentTargetBubblePhaseInvokeLater (selector, method) {

        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectAll(selector);
        this.addEventListener(selected);

    }

    SelectAllCurrentTargetBubblePhaseInvokeNow (selector, method) {

        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectAll(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);

    }

    SelectAllCurrentTargetCapturePhaseInvokeLater (selector, method) {

        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectAll(selector);
        this.addEventListener(selected);

    }

    SelectAllCurrentTargetCapturePhaseInvokeNow (selector, method) {

        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectAll(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);

    }

    SelectFirstEventTargetBubblePhaseInvokeLater (selector, method) {

        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectFirst(selector);
        this.addEventListener(selected);

    }

    SelectFirstEventTargetBubblePhaseInvokeNow (selector, method) {

        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectFirst(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);

    }

    SelectFirstEventTargetCapturePhaseInvokeLater (selector, method) {

        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectFirst(selector);
        this.addEventListener(selected);

    }

    SelectFirstEventTargetCapturePhaseInvokeNow (selector, method) {

        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectFirst(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);

    }

    SelectFirstCurrentTargetBubblePhaseInvokeLater (selector, method) {

        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectFirst(selector);
        this.addEventListener(selected);

    }

    SelectFirstCurrentTargetBubblePhaseInvokeNow (selector, method) {

        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectFirst(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);

    }

    SelectFirstCurrentTargetCapturePhaseInvokeLater (selector, method) {

        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectFirst(selector);
        this.addEventListener(selected);

    }

    SelectFirstCurrentTargetCapturePhaseInvokeNow (selector, method) {

        const selected = EventListener.selectFirst(selector);
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.capturePhase();
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);

    }

    static eventTarget (method) {

        return function anonymous (event) {

            return method(event);

        };

    }

    static currentTarget (method) {

        return function anonymous (event) {

            return method(event.currentTarget);

        };

    }

    static invokeNow (selected, method) {

        selected.forEach((element) => {

            method(element);

        });

    }

    static bubblePhase () {

        return false;

    }

    static capturePhase () {

        return true;

    }

    static selectAll (selector) {

        const array = [];
        return array.slice.call(document.querySelectorAll(selector));

    }

    static selectFirst (selector) {

        return [document.querySelector(selector)];

    }

}
