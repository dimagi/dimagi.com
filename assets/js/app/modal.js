/* global console */
define([
  'jquery',
  'lodash',
], function ($, _) {
  'use strict';
  var modals = {};

  var Modal = function (element) {
    var modal = this;
    modal.$modal = $(element);
    modal.id = modal.$modal.attr("id");

    if (!modal.id) throw "Modal element requires an ID attribute!";

    modals[_.camelCase(modal.id)] = modal;
    modal.$wrapper = modal.$modal.find(".modal-wrapper");
    console.log(modal.$modal);
    modal.$closeButton = modal.$modal.find(".modal-close-button");
    modal.$focusEl = modal.$modal.find("[data-modal-focus]").first();
    modal.hasCloseButton = modal.$closeButton.length;
    modal.$triggers = $("[href='#" + modal.id + "'], [data-modal='" + modal.id + "']");
    modal.dismissible = Boolean(modal.$modal.data("dismissible"));
    modal.activateCallbacks = [];
    modal.deactivateCallbacks = [];
    modal.responseCallbacks = [];

    modal.initialize = function () {
      modal.setupTriggerLinks();
      if (modal.dismissible) {
        modal.addCloseButton();
      }
      modal.enableBindings();
    };

    modal.enableBindings = function () {
      $(document).on("click", "[data-modal='" + modal.id + "']", function (e) {
        modal.activate();
        e.preventDefault();
      });
      modal.$modal.on("click", "[data-modal-confirm='" + modal.id + "']", function (e) {
        modal.setResponse(true);
        modal.deactivate();
        if(!$(e.currentTarget).is('a[href]:not([href="#"])')) {
          e.preventDefault();
        }
      });
      modal.$modal.on("click", "[data-modal-dismiss='" + modal.id + "']", function (e) {
        modal.setResponse(false);
        modal.deactivate();
        e.preventDefault();
      });
      console.log(modal.$closeButton);
      modal.$closeButton.on("click", function(e) {
        modal.dismiss();
        e.preventDefault();
      });
      modal.$modal.on("click", function(e) {
        if (e.target.id === modal.id) {
          modal.dismiss();
        }
      });
      $(document).on("keydown", function (e) {
        if (e.keyCode === 27) {
          modal.dismiss();
        }
      });
    };

    modal.activate = function () {
      modal.active = true;
      modal.activateHandler();
      modal.toggleModalState();
    };

    modal.dismiss = function () {
      if (modal.dismissible) {
        modal.deactivate();
      } else {
        modal.makeItBounce();
      }
    };

    modal.deactivate = function () {
      modal.active = false;
      modal.deactivateHandler();
      modal.toggleModalState();
    };

    modal.toggleModalState = function () {
      modal.$modal.attr("data-active", modal.active);
      $("html").toggleClass("modal-active", modal.active);
      if (modal.active && !window.Modernizr.touch) {
        modal.$focusEl.focus();
      }
    };

    modal.makeItBounce = function () {
      modal.$wrapper.one(
        "animationend webkitAnimationEnd oanimationend MSAnimationEnd",
        function () {
          modal.$modal.removeClass("shake");
        }
      );
      modal.$modal.addClass("shake");
    };

    modal.addCloseButton = function () {
      var $elem;
      if (!modal.hasCloseButton) {
        $elem = $('<a href="#" class="modal-close-button" />');
        if (modal.$wrapper.length) {
          modal.$wrapper.prepend($elem);
        } else {
          modal.$modal.prepend($elem);
        }
      }
      modal.$closeButton = modal.$modal.find(".modal-close-button");
    };

    modal.setResponse = function (response) {
      modal.response = response;
      modal.responseHandler();
    };

    modal.activateHandler = function () {
      $.each(modal.activateCallbacks, function() {
          return _.isFunction(this) ?  console.log(this + " is not a function") : this.call();
      });
    };

    modal.deactivateHandler = function () {
      $.each(modal.deactivateCallbacks, function() {
          return _.isFunction(this) ?  console.log(this + " is not a function") : this.call();
      });
    };

    modal.responseHandler = function () {
      $.each(modal.responseCallbacks, function() {
          return _.isFunction(this) ?  console.log(this + " is not a function") : this.call();
      });
    };

    modal.onActivate = function (fn) {
      modal.activateCallbacks.push(fn);
    };

    modal.onDeactivate = function (fn) {
      modal.deactivateCallbacks.push(fn);
    };

    modal.onResponse = function (fn) {
      modal.responseCallbacks.push(fn);
    };

    modal.setupTriggerLinks = function () {
      modal.$triggers.attr("data-modal", modal.id);
    };

  };

  return {
    initialize: function () {
      $(".modal").each(function () {
        var newModal = new Modal(this);
        newModal.initialize();
      });
    },
  };
});
