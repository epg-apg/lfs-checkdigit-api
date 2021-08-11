function calculateCheckdigit1(number) {
    let numberStr = number.toString();
	
	if(numberStr.length != 9) {
		return -1;
	}
	
    let sum = 0;

    for (i = numberStr.length; i > 0; i--) {
        if (i % 2 == 0) {
            sum += parseInt(numberStr.substr(i-1, 1)) * 1;
        } else {
            sum += parseInt(numberStr.substr(i-1, 1)) * 3;
        }
    }

    checkdigit = 10 - sum % 10;

    return checkdigit;
}

function calculateLFSCheckdigit(lfsNumber, mode) {
    let number = "";
    if (lfsNumber.length === 12) {
        number = lfsNumber.substr(2, 9);
    } else if (lfsNumber.length === 11) {
        number = lfsNumber.substr(2, 9);
    } else if (lfsNumber.length <= 9) {
        number = lfsNumber;
    } else {
        return -1;
    }

	//TODO padding to 9 characters
    if (mode === 1) {
        return calculateCheckdigit1(number);
    }
    else {
        return -1;
    }
}