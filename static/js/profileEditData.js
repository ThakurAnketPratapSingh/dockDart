let img=document.querySelector("#imgid");
let file=document.querySelector("#img1");

file.addEventListener('change',function(){
    const choosedFile=this.files[0];
    if(choosedFile){
        let reader=new FileReader();
        reader.addEventListener('load',function(){
            img.setAttribute('src',reader.result);
        });
        reader.readAsDataURL(choosedFile);
    }

});