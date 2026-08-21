/* Elizabeth Tesfaye Law Office — site behaviour
   Vanilla JS, no dependencies, no cookies, no tracking. */
(function () {
  'use strict';

  /* ---- Mobile navigation ---- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('primary-nav');

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!open));
      nav.classList.toggle('is-open', !open);
      document.body.style.overflow = !open ? 'hidden' : '';
    });

    // Close when a link is tapped
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('is-open');
        document.body.style.overflow = '';
      }
    });

    // Close on Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('is-open');
        document.body.style.overflow = '';
        toggle.focus();
      }
    });

    // Reset when resizing up to desktop
    var mq = window.matchMedia('(min-width: 1001px)');
    var reset = function () {
      if (mq.matches) {
        toggle.setAttribute('aria-expanded', 'false');
        nav.classList.remove('is-open');
        document.body.style.overflow = '';
      }
    };
    mq.addEventListener ? mq.addEventListener('change', reset) : mq.addListener(reset);
  }

  /* ---- Header shadow on scroll ---- */
  var header = document.querySelector('.site-header');
  if (header) {
    var onScroll = function () {
      header.classList.toggle('is-scrolled', window.scrollY > 12);
    };
    onScroll();
    window.addEventListener('scroll', onScroll, { passive: true });
  }

  /* ---- Reveal on scroll ---- */
  var reveals = document.querySelectorAll('.reveal');
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (reveals.length && 'IntersectionObserver' in window && !reduced) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

    reveals.forEach(function (el, i) {
      el.style.transitionDelay = Math.min(i % 3, 2) * 90 + 'ms';
      io.observe(el);
    });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ---- Whole-card click target ---- */
  document.querySelectorAll('.card--stretch').forEach(function (card) {
    var link = card.querySelector('a[href]');
    if (!link) return;
    card.addEventListener('click', function (e) {
      if (e.target.closest('a')) return;
      link.click();
    });
  });

  /* ---- Language: English / Amharic ---- */
  var root = document.documentElement;
  var stored = localStorage.getItem('et-lang');
  var setLang = function (lang) {
    lang = lang === 'am' ? 'am' : 'en';
    root.setAttribute('lang', lang);
    localStorage.setItem('et-lang', lang);
    document.querySelectorAll('.lang-toggle[data-lang]').forEach(function (btn) {
      btn.classList.toggle('is-active', btn.getAttribute('data-lang') === lang);
    });
  };
  if (stored === 'am' || stored === 'en') setLang(stored);
  document.querySelectorAll('.lang-toggle[data-lang]').forEach(function (btn) {
    btn.addEventListener('click', function () { setLang(btn.getAttribute('data-lang')); });
  });

  /* ---- Footer year ---- */
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
