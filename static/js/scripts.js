function valSelection()  
{  
    var selected = document.getElementsByName("symptoms");  
    var numberOfCheckedItems = 0;  
    for(var i = 0; i < selected.length; i++)  
    {  
        if(selected[i].checked)  
            numberOfCheckedItems++;  
    }  
    if(numberOfCheckedItems > 2)  
    {  
        alert("You can't select more than two symtoms!");  
        return false;  
    }  
};

function checkEmptyValue(){
    var fname = document.getElementsByName("firstname");
    var lname = document.getElementsByName("lastname");
    var country = document.getElementsByName("country");
    var subject = document.getElementsByName("subject");
    if(fname=="" || lname=="" || country=="" || subject==""){
        alert("Complete this form");  
        return false; 
    }
    if(fname!="" && lname!="" && country!="" && subject!=""){
        alert("Yout subject submitted");  
        return true; 
    }
};