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

$(document).ready(function(){
    
    var TagJob = Spine.Model.sub();
    TagJob.configure("TagJob", "taglines", "format", "outputfile", "generated");
    TagJob.extend(Spine.Model.Ajax);
    
    TagJob.extend({
        url: "/clustering/api/pca/tagjob/"
    });
    
    var TagJobs = Spine.Controller.sub({
        events: {"form#pca_form": "create"},

        create: function(e) {
          
          console.info('asasca');
          e.preventDefault();
          var tagJob = TagJob.fromForm(e.target)
          
          console.info(tagJob);
          
          tagJob.save();
        }
      });
    
    
    jobs = new TagJobs;
    
    
    aJob = TagJob.init({taglines: "addyosmani, addyosmani addyosmani", format: "png"});  
    aJob.save();
    
    console.info(aJob);
    
});