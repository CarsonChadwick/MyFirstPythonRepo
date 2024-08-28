let raceNumber = Math.floor(Math.random() * 1000);
var registeredEarly = false;
var runnerAge = 18;
if (runnerAge > 18 && registeredEarly)
{
  raceNumber += 1000;
}
if (runnerAge > 18 && registeredEarly)
{
  console.log("You will run at 9:30am. Your race number is " + raceNumber);
}
else if (runnerAge >18)
{
  console.log("You will run at 11:00am. Your race number is " + raceNumber);
}
else if (runnerAge === 18);
{
  console.log("See the registration desk.")
}
else
{
  console.log("Your race starts at 12:30. Your race number is " + raceNumber);
}