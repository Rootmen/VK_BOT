(function() {

    var input_group = $("#input-group");
    var btnSubmit = $("#news-submit");
    

    input_group.change(function (e) {
        if(/[А-ЯЁ]{3}-[0-5]{1}[0-9]{2}/g.test($(this).val())) {
            DOM.setInputValid($(this));
            DOM.disable(btnSubmit);
        } else {
            DOM.setInputInvalid($(this));
            DOM.enable(btnSubmit);
        }
    });
})();