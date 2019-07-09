let pizzaReviewB = `
<div id="pizza2" class="card mb-3" style="max-width:80%;">
  <div class="row no-gutters">
    <div class="col-md-4">
      <img src="images/pizza.jpg" class="card-img" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">Pepe's Pizzeria</h5>
        <p class="card-text">let me start by saying I intend on providing a thorough review of my experience with one caveat, I am not from the area so have no local comparison.

FIRST, I like this place and recommend to locals and passerbys to come support them as they are 2 months into operations...now let me verbose and break it down.....

SERVICE: absolutely off the charts! I can say that I am leave knowing the names of everyone; hostess, sommelier, waitress, plus some bonus peeps. A team that truly cares (i.e. bending down to pick a little odd and end of the floor and not just walk by)

AMBIENCE: superb, front area has a lively bar and some table seating just removed via a half wall partition from the bar for a more casual dining experience. Past the wine cellar there is a more formal dining room. Really designed to cater to a variety of dining experiences. One opportunity is to improve the workflow in the hallway that connects the front with the dining room and restroom....A little chaotic.

FOOD: solid, but not blow your mind away. The oysters are out of sight. Had a filet, the cast iron is  a neat concept, however, this causes the different food to have varying temps (i.e. vegetables are burn your mouth, potatoes are manageable and steak is perfect). The menu suggests the steak is "encrusted with black pepper", but not sure I tasted any black pepper....need to change that descriptor....on the flip side no shortage of garlic. At $45 for a 12 oz, the quality of the cut could be improved. Some very creative desserts. All in all food is good, some great concepts, need to fine tune execution.

LASTLY: I do despise having a $150+/pp meal and the check being dropped off when you are still eating with the, "no rush, I am just leaving this for you".....maybe if it is after hours but not during operating hours...however this is both personal preference and easily corrected....

Giving it 4 stars and believe to could be 5 stars in time...
</p>
        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
      </div>
    </div>
  </div>
</div>
`
let pizzaReviewS = `
<div id="pizza" class="card mb-3" style="max-width:80%;">
  <div class="row no-gutters">
    <div class="col-md-4">
      <img src="images/pizza.jpg" class="card-img" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">Pepe's Pizzeria</h5>
        <p class="card-text">Let me start by saying I intend on providing a thorough review of my experience with one caveat, I am not from the area so have no local comparison. FIRST, I like this place and recommend to locals and passerbys to
          come support...</p>
        <p class="card-text"><small class="text-muted">Last updated 3 mins ago</small></p>
      </div>
    </div>
  </div>
</div>
`
$(document).ready(function() {
  $("#pizza").click(function() {
    $("#blogs").empty();
    $("#blogs").append(pizzaReviewB);

  });
  $("#pizza2").click(function() {
    $("#blogs").empty();
    $("#blogs").append(pizzaReviewS);

  });
});
