export class EventListener {
    private addEventListener(selected: Element[]) {
        selected.forEach((element: Element) => {
            element.addEventListener(this.type, this.callback, this.capture);
        });
    }
    private static eventTarget(method: (argument: Event) => void) {
        return (event: Event) => method(event);
    }
    private static currentTarget(method: (argument: EventTarget) => void) {
        return (event: Event) => method(event.currentTarget);
    }
    private static invokeNow(selected: Element[], method: (argument: Event | EventTarget) => void) {
        selected.forEach((element: Element) => {
            method(element);
        });
    }
    private static bubblePhase() {
        return false;
    }
    private static capturePhase() {
        return true;
    }
    private static selectAll(selector: string) {
        let array = [];
        return array.slice.call(document.querySelectorAll(selector));
    }
    private static selectFirst(selector: string) {
        return [document.querySelector(selector)];
    }
    type: string;
    callback: (event: Event) => void;
    capture: boolean;
    public SelectAllEventTargetBubblePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectAll(selector);
        this.addEventListener(selected);
    }
    public SelectAllEventTargetBubblePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectAll(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);
    }
    public SelectAllEventTargetCapturePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectAll(selector);
        this.addEventListener(selected);
    }
    public SelectAllEventTargetCapturePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectAll(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);
    }
    public SelectAllCurrentTargetBubblePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectAll(selector);
        this.addEventListener(selected);
    }
    public SelectAllCurrentTargetBubblePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectAll(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);
    }
    public SelectAllCurrentTargetCapturePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectAll(selector);
        this.addEventListener(selected);
    }
    public SelectAllCurrentTargetCapturePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectAll(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);
    }
    public SelectFirstEventTargetBubblePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectFirst(selector);
        this.addEventListener(selected);
    }
    public SelectFirstEventTargetBubblePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectFirst(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);
    }
    public SelectFirstEventTargetCapturePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectFirst(selector);
        this.addEventListener(selected);
    }
    public SelectFirstEventTargetCapturePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.eventTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectFirst(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);
    }
    public SelectFirstCurrentTargetBubblePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectFirst(selector);
        this.addEventListener(selected);
    }
    public SelectFirstCurrentTargetBubblePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.bubblePhase();
        const selected = EventListener.selectFirst(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);
    }
    public SelectFirstCurrentTargetCapturePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectFirst(selector);
        this.addEventListener(selected);
    }
    public SelectFirstCurrentTargetCapturePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        this.callback = EventListener.currentTarget(method);
        this.capture = EventListener.capturePhase();
        const selected = EventListener.selectFirst(selector);
        EventListener.invokeNow(selected, method);
        this.addEventListener(selected);
    }
}