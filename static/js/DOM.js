(function () {
    var DOM = {
        empty: '',
    
        isInvalid: 'is-invalid',
        isValid: 'is-valid',
        disabled: 'disabled',
    
        /* attributes */
    
        enable: function (elem) {
            elem.removeAttr(DOM.disabled);
        },
        
        disable: function(elem) {
            elem.attr(DOM.disabled, DOM.empty);
        },
    
    
        /* classes */
    
        setInputValid: function (elem) {
            valid(elem, true);
        },
        
        setInputInvalid: function (elem) {
            valid(elem, false);
        },


        
    };

    
    /* internal methods */

    function valid(elem, flag) { 
        setClasses(elem, DOM.isValid, DOM.isInvalid, flag);
    }

    function toggleClass (elem, attr, flag) {
        if(flag) {
            elem.addClass(attr);
        } else {
            elem.removeClass(attr);
        }
    }

    function setClasses(elem, attrTrue, attrFalse, flag) {
        if(flag) {
            elem.removeClass(attrFalse);
            elem.addClass(attrTrue);
        } else {
            elem.removeClass(attrTrue);
            elem.addClass(attrFalse);
        }
    }

    window.DOM = DOM;
})();