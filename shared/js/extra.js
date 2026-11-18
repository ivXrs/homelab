/* Homelab docs: scroll reveal + language switcher fix. Vanilla JS, no deps. */
(function () {
  "use strict";

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var observer = null;

  function revealInit() {
    if (observer) { observer.disconnect(); observer = null; }
    if (reduce.matches || !("IntersectionObserver" in window)) return;

    var root = document.querySelector(".md-content__inner");
    if (!root) return;

    observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("hl-in");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -5% 0px" });

    var targets = root.querySelectorAll(
      ":scope > h2, :scope > h3, :scope > p, :scope > .md-typeset__scrollwrap, :scope > table, " +
      ":scope > .admonition, :scope > .highlight, img.reveal, .grid.cards > ul > li"
    );
    targets.forEach(function (el) {
      if (el.closest(".hero")) return;
      if (el.classList.contains("md-typeset__scrollwrap")) {
        el = el.querySelector("table") || el;
      }
      if (el.tagName === "TABLE") {
        el.querySelectorAll("tbody tr").forEach(function (tr, n) {
          tr.style.setProperty("--row", n);
        });
      }
      if (el.matches(".grid.cards > ul > li")) {
        var idx = Array.prototype.indexOf.call(el.parentNode.children, el);
        el.style.setProperty("--hl-delay", (idx * 90) + "ms");
      }
      el.classList.add("hl-reveal");
      observer.observe(el);
    });
  }

  // Keep the current page when switching language (/en/x/ <-> /es/x/).
  function langSwitcherInit() {
    var m = location.pathname.match(/^(.*?\/)(en|es)(\/.*)?$/);
    if (!m) return;
    document.querySelectorAll(".md-select__link[hreflang]").forEach(function (a) {
      a.setAttribute("href", m[1] + a.getAttribute("hreflang") + (m[3] || "/") + location.search + location.hash);
    });
  }

  function init() {
    revealInit();
    langSwitcherInit();
  }

  // Zensical instant navigation exposes document$; fall back to plain load.
  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(init);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
