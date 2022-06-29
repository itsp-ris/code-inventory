package game;

import java.util.ArrayList;
import java.util.List;

import edu.monash.fit2099.engine.Actions;
import edu.monash.fit2099.engine.Actor;
import edu.monash.fit2099.engine.Ground;
import edu.monash.fit2099.engine.Item;
import edu.monash.fit2099.engine.Location;
import edu.monash.fit2099.interfaces.FoodInterface;
import edu.monash.fit2099.interfaces.ItemInterface;

/**
 * Class representing the Shop.
 */
public class Shop extends Ground {
	private static ArrayList<ItemInterface> stockItems = new ArrayList<ItemInterface>();
	
	/**
	 * Constructor.
	 * A Shop is displayed as 'S' on the map.
	 */
	public Shop() {
		super('S');
	}
	
	static {
		//Creates Egg stocks in the Shop for Actors to buy 
		Egg protoEgg = new Egg("Protoceratops' egg", '*', new Protoceratops("Baby Protoceratops", 0));
		Egg	veloEgg = new Egg("Velociraptors' egg", '*', new Velociraptors("Baby Velociraptors", 0));
		Egg plesioEgg = new Egg("Plesiosaurs' egg", '*', new Plesiosaurs("Baby Plesiosaurs", 0));
		Egg pteaEgg = new Egg("Pteanodons' egg", '*', new Pteranodons("Baby Pteanodons", 0));
		Egg trexEgg = new Egg("T-Rex's egg", '*', new TRex("Baby TRex", 0));
		
		//Creates Food stocks in the Shop for Actors to buy
		Food herbivoreFood = new Food("Herbivore's food", '"', 100, 20, 0);
		Food carnivoreFood = new Food("Carnivore's food", '"', 100, 100, 0);
		Food marineFood = new Food("Marine Food", '"', 150, 200, 0);
		
		//Creates dinosaur tag for Actors to obtain
		PortableDinoItem dinosaurTag = new PortableDinoItem("Dinosaur Tag", '|', 0, 0);
		
		stockItems.add(protoEgg);
		stockItems.add(veloEgg);
		stockItems.add(plesioEgg);
		stockItems.add(pteaEgg);
		stockItems.add(trexEgg);
		stockItems.add(herbivoreFood);
		stockItems.add(carnivoreFood);
		stockItems.add(dinosaurTag);
	}
	
	/**
	 * Returns a list of Actions for adjacent Actors to perform
	 * @param actor		The Actor acting
	 * @param location  The current Location
	 * @param direction The direction of the Ground from the Actor
	 *  @return a collection of Actions
	 */
	@Override
	public Actions allowableActions(Actor actor, Location location, String direction) {
		Actions actions = super.allowableActions(actor, location, direction);
		
		//Allows only Player to buy and sell
		if (actor instanceof Player) {	
			for (ItemInterface item : stockItems) {
				actions.add(new BuyAction(item));
			}
			
			List<Item> inventory = actor.getInventory();
			
			for (Item item : inventory) {
				if (item instanceof ItemInterface) {
					actions.add(new SellAction((ItemInterface) item));
				}
			}
		}
		
		return actions;
	}
	
	/**
	 * Returns false to indicate that Actor cannot enter
	 * @param actor the incoming Actor
	 */
	@Override
	public boolean canActorEnter(Actor actor) {
		return false;
	}
}
