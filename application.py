"""Quick test of selected applications."""

import celestine

celestine.main(["-l", "en"], True)
celestine.main(["-a", "demo", "-l", "en"], True)
celestine.main(["-a", "viewer", "-l", "en"], True)
