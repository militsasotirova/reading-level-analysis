$(document).ready(function(){
  //This does not set the label to the active position:
  //$('.input-field label').addClass('active');
  
  //This does set the label to the active position.
  setTimeout(function(){ $('.input-field label').addClass('active'); }, 1);
});
/*
$(document).ready(function() {
    $('textarea#text').keypress(function() {
        getReadingLevel($('textarea#text').val());
    });
});
*/
 $(document).ready(function() 
 {
    $("#submit").click(function() {
    	getReadingLevel( $('textarea#text').val() );
 	});
    $("#greek").click(function() {
    	document.getElementById("text").value = "The rule of rhythm in prose is not so intricate. Here, too, we write in groups, or phrases, as I prefer to call them, for the prose phrase is greatly longer and is much more nonchalantly uttered than the group in verse; so that not only is there a greater interval of continuous sound between the pauses, but, for that very reason, word is linked more readily to word by a more summary enunciation. Still, the phrase is the strict analogue of the group, and successive phrases, like successive groups, must differ openly in length and rhythm. The rule of scansion in verse is to suggest no measure but the one in hand; in prose, to suggest no measure at all. Prose must be rhythmical, and it may be as much so as you will; but it must not be metrical. It may be anything, but it must not be verse.";
    	//getReadingLevel($('textarea#text').val());
    });
    $("#winnie").click(function() {
    	document.getElementById("text").value = 'In after-years he liked to think that he had been in Very Great Danger during the Terrible Flood, but the only danger he had really been in was the last half-hour of his imprisonment, when Owl, who had just flown up, sat on a branch of his tree to comfort him, and told him a very long story about an aunt who had once laid a seagull\'s egg by mistake, and the story went on and on, rather like this sentence, until Piglet who was listening out of his window without much hope, went to sleep quietly and naturally, slipping slowly out of the window towards the water until he was only hanging on by his toes, at which moment, luckily, a sudden loud squawk from Owl, which was really part of the story, being what his aunt said, woke the Piglet up and just gave him time to jerk himself back into safety and say, "How interesting, and did she?" when — well, you can imagine his joy when at last he saw the good ship, Brain of Pooh (Captain, C. Robin; 1st Mate, P. Bear) coming over the sea to rescue him.';
    	//getReadingLevel($('textarea#text').val());
    });
    $("#age").click(function() {
    	document.getElementById("text").value = 'Therefore, whenever anything happened that Mrs. Archer wanted to know about, she asked Mr. Jackson to dine; and as she honoured few people with her invitations, and as she and her daughter Janey were an excellent audience, Mr. Jackson usually came himself instead of sending his sister. If he could have dictated all the conditions, he would have chosen the evenings when Newland was out; not because the young man was uncongenial to him (the two got on capitally at their club) but because the old anecdotist sometimes felt, on Newland\'s part, a tendency to weigh his evidence that the ladies of the family never showed.';
    	//getReadingLevel($('textarea#text').val());
    });
    $("#clear").click(function() {
    	document.getElementById("text").value = '';
    	$("#sentences").text("Number of Sentences: 0");
        $("#words").text("Number of Words: 0");
        $("#chars").text("Number of Characters: 0");
        $("#rlevel").text("Automated Readability Index: 0");
        $("#clauses").text("Number of Clauses: 0");
        $("#clausesPerSent").text("Clauses Per Sentence: 0");
        $("#avgFrequency").text("Average Word Frequency: 0");
        $("#finalReadingLevel").text("Final Reading Level: 0");
    });
});

function getReadingLevel(text) {

	var url = 'level?text=' + encodeURIComponent(text);//var url = '/analysis/level?text=' + encodeURIComponent(text);
console.log("chckpt 1");
	$.ajax(url, {dataType: 'json'})

 	.done(function(result, status, json) {
 		console.log("chckpt 2");
        var statistics = json.responseJSON;
        console.log("chckpt 3");
        $("#sentences").text("Number of Sentences: " + statistics.sentences);
        $("#words").text("Number of Words: " + statistics.words);
        $("#chars").text("Number of Characters: " + statistics.chars);
        $("#rlevel").text("Automated Readability Index: " + statistics.level);
        $("#clauses").text("Number of Clauses: " + statistics.clauses);
        $("#clausesPerSent").text("Clauses Per Sentence: " + statistics.clausesPerSent);
        $("#avgFrequency").text("Average Word Frequency: " + statistics.avg_frequency);
        $("#finalReadingLevel").text("Final Reading Level: " + statistics.final_reading_level);
  	})

    .fail(function(error) {
        console.log(typeof error);
        console.log(error);
    })

    .always(function(data) {
        //console.log(typeof data);
    });

}