$( document ).ready(function() {

$( "#select_type" ).change(function(){
    if ($( "#select_type" ).val() == "PF"){
        $("#label_tipo").show();
        $("#label_tipo").text("CPF");
        $("#input_cpf").show();
        $("#label_nome").text("Nome Completo");
        $("#id_nome").show();
        $("#id_razao_social").hide();
        $("#help").show();
        $("#help").text("Desejável nome completo para envio do boleto");
        $("#input_cnpj").hide();
        $("#panel_profile").removeAttr('hidden');
        $("#panel_title").text('Pessoa Física');
    }
    else if ($( "#select_type" ).val() == "PJ"){
        $("#label_tipo").show();
        $("#label_tipo").text("CNPJ");
        $("#input_cnpj").show();
        $("#label_nome").text("Razão Social");
        $("#id_razao_social").show();
        $("#id_nome").hide();
        $("#help").show();
        $("#help").text("Razão Social");
        $("#input_cpf").hide();
        $("#panel_profile").removeAttr('hidden');
        $("#panel_title").text('Pessoa Jurídica');
        }
    else{
    $("#panel_profile").attr("hidden", "true");

    }
}
)

if ($('#id_nome').val() == '' && ($('#id_razao_social').val() != '') ) {
    $("#select_type").val("PJ");
    $("#label_tipo").show();
    $("#label_tipo").text("CNPJ");
    $("#input_cnpj").show();
    $("#label_nome").text("Razão Social");
    $("#id_razao_social").show();
    $("#id_nome").hide();
    $("#help").show();
    $("#help").text("Razão Social");
    $("#input_cpf").hide();
    $("#panel_profile").removeAttr('hidden');
    $("#panel_title").text('Pessoa Jurídica');

}

if ($('#id_razao_social').val() == '' && ($('#id_nome').val() != '') ) {
    $("#select_type").val("PF");
    $("#label_cpf").show();
    $("#label_tipo").show();
    $("#label_tipo").text("CPF");
    $("#input_cpf").show();
    $("#label_nome").text("Nome Completo");
    $("#id_nome").show();
    $("#id_nome").attr('placeholder','Nome completo');
    $("#id_razao_social").hide();
    $("#help").show();
    $("#input_cnpj").hide();
    $("#panel_profile").removeAttr('hidden');
    $("#panel_title").text('Pessoa Física');

}

if ($('#id_razao_social').val() == '' && ($('#id_nome').val() == '') ) {
        $("#select_type").val("");
        $("#label_cpf").hide();
        $("#input_cpf").hide();
        $("#id_nome").hide();
        $("#help").hide();
        $("#label_cnpj").hide();
        $("#input_cnpj").hide();
        $("#id_razao_social").hide();

}

$("#btn-submit").click(function() {
if ($( "#select_type" ).val() == "PF" && $("#input_cpf").val().length > 0 && $("#id_nome").val().length > 0 )
    {

        $("#input_cnpj").val("");
        $("#id_razao_social").val("");
    }

else if ($( "#select_type" ).val() == "PJ" && $("#input_cnpj").length > 0 && $("#id_razao_social").val().length > 0 )
    {
        $("#input_cpf").val("");
        $("#id_nome").val("");
    }

})

});
