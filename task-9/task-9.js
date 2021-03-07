//open up telegram web and go to the chat you want to spam 
//open console ( Ctrl + Shift + J )
//execute the code 
var x = "Hi"; //spam message 
var y = Math.random(); //sets the interval to a random number less than 1
var z = Math.floor(Math.random() * 100) + 1; //returns a random integer from 1 to 100, is the number of times to send
var n = z ; //notify 
var i = 0 ;
var timer = setInterval(function(){
	document.getElementsByClassName('composer_rich_textarea')[0].innerHTML = x;	//copies the message into the text box
	$('.im_submit').trigger('mousedown');	//triggers a mousedown event in the submit button
	i++;	//keeps the count of messages
	if( i  == z )	//if i reaches the desired number of times, it stops the iteration
	clearInterval(timer);
	if( i % n == 0)	//after the iteration stops, the line displays the number of messages sent in the console
	console.log(i + ' MESSAGES SENT');
} , y * 1000 )
