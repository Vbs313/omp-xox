// omp-xox v3: Dev Tools — test-runner with framework auto-detection

import type { ExtensionAPI } from "@oh-my-pi/pi-coding-agent";
import testRunner from "./test-runner.ts";

export default function devTools(pi: ExtensionAPI) {
  pi.setLabel("omp-xox Test Runner");
  testRunner(pi);
}
