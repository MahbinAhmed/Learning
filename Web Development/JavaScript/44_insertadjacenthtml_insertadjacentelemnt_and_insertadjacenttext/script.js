let section = document.getElementsByTagName("section")[0];
section.insertAdjacentHTML("beforebegin", "<p>Before Begin</p>");
section.insertAdjacentHTML("afterbegin", "<p>After Begin</p>");
section.insertAdjacentHTML("beforeend", "<p>Before End</p>");
section.insertAdjacentHTML("afterend", "<p>After End</p>");
section.remove();