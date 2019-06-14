export class EventListener {
    private static addEventListener(selected: Element[], type: string, callback: (event: Event) => void, capture: boolean) {
        selected.forEach((element: Element) => {
            element.addEventListener(type, callback, capture);
        });
    }
    private static EventTarget(method: (argument: Event) => void) {
        return (event: Event) => method(event);
    }
    private static CurrentTarget(method: (argument: EventTarget) => void) {
        return (event: Event) => method(event.currentTarget);
    }
    private static InvokeLater(selected: Element[], method: (argument: Event | EventTarget) => void) {
        method;
        selected.forEach((element: Element) => {
            element;
        });
    }
    private static InvokeNow(selected: Element[], method: (argument: Event | EventTarget) => void) {
        selected.forEach((element: Element) => {
            method(element);
        });
    }
    private static BubblePhase() {
        return false;
    }
    private static CapturePhase() {
        return true;
    }
    private static SelectAll(selector: string) {
        let array = [];
        return array.slice.call(document.querySelectorAll(selector));
    }
    private static SelectFirst(selector: string) {
        return [document.querySelector(selector)];
    }
    public SelectAllEventTargetBubblePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(selector);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeLater(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectAllEventTargetBubblePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(selector);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeNow(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectAllEventTargetCapturePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(selector);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeLater(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectAllEventTargetCapturePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(selector);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeNow(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectAllCurrentTargetBubblePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(selector);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeLater(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectAllCurrentTargetBubblePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(selector);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeNow(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectAllCurrentTargetCapturePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(selector);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeLater(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectAllCurrentTargetCapturePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectAll(selector);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeNow(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectFirstEventTargetBubblePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(selector);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeLater(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectFirstEventTargetBubblePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(selector);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeNow(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectFirstEventTargetCapturePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(selector);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeLater(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectFirstEventTargetCapturePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(selector);
        var callback = EventListener.EventTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeNow(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectFirstCurrentTargetBubblePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(selector);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeLater(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectFirstCurrentTargetBubblePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(selector);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.BubblePhase();
        EventListener.InvokeNow(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectFirstCurrentTargetCapturePhaseInvokeLater(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(selector);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeLater(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
    public SelectFirstCurrentTargetCapturePhaseInvokeNow(selector: string, type: string, method: (argument: Event | EventTarget) => void) {
        var selected = EventListener.SelectFirst(selector);
        var callback = EventListener.CurrentTarget(method);
        var capture = EventListener.CapturePhase();
        EventListener.InvokeNow(selected, method);
        EventListener.addEventListener(selected, type, callback, capture);
    }
}