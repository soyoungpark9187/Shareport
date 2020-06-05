
    downloadButton.addEventListener('click', function(){
       var fileRef = storage.ref(user_name+'/'+file_name+"/"+"main/"+file_name);

       fileRef.getDownloadURL().then(function(url) {

         database.ref('report/'+onlyName+"/buyer/"+buyer).set({
            part:'main'
      });
       console.log("download");
       console.log(url);
       window.location = url;
       })
    });
    downloadseg1Button.addEventListener('click', function(){
       var fileRef = storage.ref(user_name+'/'+file_name+"/"+"seg1");

       fileRef.getDownloadURL().then(function(url) {
      database.ref('report/'+onlyName+"/buyer/"+buyer).set({
             part:'seg1'
       });
       console.log("download");
       console.log(url);
       window.location = url;
       })
    });
    downloadseg2Button.addEventListener('click', function(){
       var fileRef = storage.ref(user_name+'/'+file_name+"/"+"seg2");
        database.ref('report/'+onlyName+"/buyer/"+buyer).set({
            part:'seg2'
      });
       fileRef.getDownloadURL().then(function(url) {

       console.log("download");
       console.log(url);
       window.location = url;
       })
    });
    downloadseg3Button.addEventListener('click', function(){
       var fileRef = storage.ref(user_name+'/'+file_name+"/"+"seg3");
        database.ref('report/'+onlyName+"/buyer/"+buyer).set({
            part:'seg3'
      });
       fileRef.getDownloadURL().then(function(url) {

       console.log("download link");
       console.log(url);
       window.location = url;
       })
    });
