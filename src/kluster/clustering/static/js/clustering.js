/*
Kluster - A clustering Web Service

Copyright (C) 2011 Atizo AG and individual contributors (see AUTHORS).

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

clustering = {};
clustering.gui = {};
clustering.gui.on_poll = false;

clustering.gui.toggle_poll = function() {
    
    if (clustering.on_poll == true) {
        $("#pca_form_submit").show();
        $("#form_submit").removeClass('loader');
        clustering.on_poll = false;
    } else {
        $("#pca_form_submit").hide();
        $("#form_submit").addClass('loader');
        clustering.on_poll = true;
    }
}

clustering.gui.handle_ouput = function(data) {
    
    var result = $('#result');
    var output = '<i>No output</i>';
    
    if (data.outputfile_url) {
        output = '<a href="'+data.outputfile_url+'">Download File</a>'
        if (data.format == 'png') {
            output += '<div class="spacer-10"></div><img src="'+ data.outputfile_url+'"/>'
        } 
    }
    result.empty();
    result.html('<div class="spacer-20"></div><div class="quote">'+output+'</div>');
}

clustering.poll_for_updates = function(job_id) {
    $presenation_interval = setInterval(function() {
        $.ajax({
            url: '/clustering/api/pca/tagjob/'+job_id+'/',
            type: 'GET',
            success: function(data) {
                if (data.done == true) {
                    clearInterval($presenation_interval);
                    clustering.gui.handle_ouput(data);
                    clustering.gui.toggle_poll();
                    
                } 
            },
            error: function(xhr_data) {
                clearInterval($presenation_interval);
                clustering.gui.toggle_poll();
            },
        }); 
    }, 2000);
}

$(document).ready(function(){
    
    $('#pca_form_submit').click(function() {
        clustering.gui.toggle_poll();
        $.ajax({
            url: '/clustering/api/pca/tagjob/',
            type: 'POST',
            data: $('#pca_form').serializeArray(),
            success: function(data) {                
                clustering.poll_for_updates(data.id);
            },
            error: function(data) {
                alert(data.responseText);
                clustering.gui.toggle_poll();
            }
        });
    }); 
    
    $('#pca_form_submit').attr("disabled", true);
    $('#id_taglines').keyup(function() {
        var text = $.trim($('#id_taglines').val());
        $('#pca_form_submit').attr("disabled", (text.length == 0));        
    });    
    
});