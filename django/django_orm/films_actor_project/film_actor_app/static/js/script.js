








function changetext(ele){
    ele_text = ele.innerText
    // console.log(ele_text   )
    // console.log(ele_text == "Show."  )
    ele.innerText = ele_text=="Show."?"Hide.":"Show.";
}