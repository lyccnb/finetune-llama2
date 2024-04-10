from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "/gpfs/data/superlab/models/llama2/llama/checkpoints/hf/Llama-2-13b-hf"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", torch_dtype="auto")

prompt = "Suppose a person has performed the given actions in the form of a sequence of action paixrs, there should be no more than two words in each action pair Each action pair is defined by a {verb} and a {noun}, separated by a space. What will be the possible next 20 actions? \You should follow the following rules: 1.For each action pairs, you can only choose the {verb} from the following words: [adjust, apply, arrange, attach, blow, break, carry, catch, clap, clean, climb, close, consume, count, cover, crochet, cut, detach, dig, dip, divide, draw, drill, drive, enter, feed, file, fill, fold, fry, give, grate, grind, hang, hit, hold, insert, inspect, iron, kick, knead, knit, lift, lock, loosen, mark, measure, mix, mold, move, open, operate, pack, paint, park, peel, pet, plant, play, point, pour, press, pull, pump, push, put, read, remove, repair, roll, sand, scoop, scrape, screw, scroll, search, serve, sew, shake, sharpen, shuffle, sieve, sit, smooth, spray, sprinkle, squeeze, stand, step, stick, stretch, swing, take, talk, throw, tie, tighten, tilt, touch, turn, turn, turn, uncover, unfold, unroll, unscrew, untie, walk, wash, water, wear, weld, wipe, write, zip] \ 2. For each action pairs, you can only choose the {noun} from the following words: [apple, apron, arm, artwork, asparagus, avocado, awl, axe, baby, bacon, bag, baking, ball, ball, balloon, banana, bar, baseboard, basket, bat, bat, bathtub, batter, battery, bead, beaker, bean, bed, belt, bench, berry, beverage, bicycle, blanket, blender, block, blower, bolt, book, bookcase, bottle, bowl, bracelet, brake, brake, branch, bread, brick, broccoli, broom, brush, bubble, bucket, buckle, burger, butter, butterfly, button, cabbage, cabinet, calculator, caliper, camera, can, candle, canvas, car, card, cardboard, carpet, carrot, cart, cat, ceiling, celery, cello, cement, cereal, chaff, chain, chair, chalk, cheese, chicken, chip, chip, chip, chisel, chocolate, chopping, chopstick, cigarette, circuit, clamp, clay, clip, clock, cloth, coaster, coconut, coffee, coffee, colander, comb, computer, container, cooker, cookie, cork, corn, corner, countertop, crab, cracker, crayon, cream, crochet, crowbar, cucumber, cup, curtain, cushion, cutter, decoration, derailleur, detergent, dice, dishwasher, dog, door, doorbell, dough, dough, doughnut, drawer, dress, drill, drill, drum, dumbbell, dust, duster, dustpan, egg, eggplant, engine, envelope, eraser, facemask, fan, faucet, fence, file, filler, filter, fish, fishing, flash, floor, flour, flower, foam, foil, food, foot, fork, fridge, fries, fuel, funnel, game, garbage, garlic, gasket, gate, gauge, gauze, gear, generator, ginger, glass, glasses, glove, glue, glue, golf, gourd, grain, grape, grapefruit, grass, grater, grill, grinder, guava, guitar, hair, hammer, hand, handle, hanger, hat, hay, haystack, head, headphones, heater, helmet, hinge, hole, horse, hose, house, ice, ice, ink, iron, jack, jacket, jug, kale, ketchup, kettle, key, keyboard, knife, label, ladder, leaf, leash, leg, lemon, lever, lid, light, lighter, lime, lock, lubricant, magnet, mango, manure, mask, mat, matchstick, meat, medicine, metal, microscope, microwave, milk, mirror, mixer, mold, money, mop, motorcycle, mouse, mouth, mower, multimeter, mushroom, nail, nail, nail, napkin, necklace, needle, net, nozzle, nut, nut, oil, okra, onion, oven, paddle, paint, paint, paintbrush, palette, pan, pancake, panel, pants, papaya, paper, pasta, paste, pastry, pea, peanut, pear, pedal, peel, peeler, peg, pen, pencil, pepper, phone, photo, piano, pickle, picture, pie, pillow, pilot, pin, pipe, pizza, planer, plant, plate, playing, plier, plug, pole, popcorn, pot, pot, potato, pump, pumpkin, purse, puzzle, rack, radio, rail, rake, razor, remote, rice, ring, rod, rolling, root, rope, router, rubber, ruler, sand, sander, sandpaper, sandwich, sauce, sausage, saw, scarf, scissors, scoop, scraper, screw, screwdriver, sculpture, seasoning, seed, set, sewing, sharpener, shears, sheet, shelf, shell, shirt, shoe, shovel, shower, sickle, sieve, sink, sketch, skirt, slab, snorkel, soap, sock, socket, sofa, soil, solder, soup, spacer, spatula, speaker, sphygmomanometer, spice, spinach, spirit, sponge, spoon, spray, spring, squeezer, stairs, stamp, stapler, steamer, steering, stick, sticker, stock, stone, stool, stove, strap, straw, string, stroller, switch, syringe, table, tablet, taco, tape, tape, tea, teapot, television, tent, test, tie, tile, timer, toaster, toilet, toilet, tomato, tongs, toolbox, toothbrush, toothpick, torch, towel, toy, tractor, trash, tray, treadmill, tree, trimmer, trowel, truck, tweezer, umbrella, undergarment, vacuum, vacuum, valve, vase, video, violin, wall, wallet, wallpaper, washing, watch, water, watermelon, weighing, welding, wheat, wheel, wheelbarrow, whisk, window, windshield, wiper, wire, wood, worm, wrapper, wrench, yam, yeast, yoghurt, zipper, zucchini].\Remember the output must be exact 20 actions in the form of {verb} and a {noun}, which means there are 19 ',' in the output. Here's the examples and question:\nexamples:\ndrive grass, pull mower, cut grass, turn mower, pull mower, pull mower, cut grass, cut grass => cut grass, drive mower, drive mower, cut grass, drive mower, cut grass, drive mower, cut mower, pull mower, cut grass, drive mower, cut grass, drive grass, cut mower, cut grass, drive mower, cut grass, drive mower, cut grass, cut grass ###\ntake sickle, cut spinach, take rubber, hold spinach, take sickle, cut spinach, put sickle, take rubber => attach spinach, put spinach, take sickle, hold spinach, cut spinach, put sickle, take rubber, tie spinach, put spinach, hold spinach, cut spinach, cut spinach, remove spinach, break rubber, take rubber, take rubber, attach rubber, put spinach, take sickle, cut spinach ###\ntake lid, open garbage, put container, put soap, take brush, put brush, put bottle, remove sponge => put container, take soap, put soap, touch faucet, open faucet, wash sponge, adjust faucet, wash sink, wash sponge, wash sink, wash sponge, wash sink, wash sponge, wash sink, wash sponge, wash sink, wash sink, wash sponge, wash sink, put bottle ###\nput mold, pour sand, remove mold, put mold, take mold, cut cement, mix cement, arrange clay => put cement, remove cement, put cement, wipe cement, carry mold, turn mold, put mold, remove sand, put mold, put mold, pour sand, take sand, wipe floor, cut cement, mix cement, arrange mold, put cement, remove cement, put cement, wipe mold ###\ndetach dough, put dough, knead dough, carry dough, put dough, knead dough, carry dough, put tray => carry table, put tray, carry table, put tray, carry tray, carry table, knead table, carry table, put dough, knead dough, knead dough, put dough, carry dough, detach dough, detach dough, put dough, detach dough, put dough, put dough, detach dough ###\nput lid, take bag, operate phone, open bag, pour seasoning, put bag, take spoon, mix food => put soup, put spoon, take container, open container, put lid, scoop pepper, pour pepper, close container, put container, take container, put lid, scoop pepper, pour pepper, cover container, take spoon, mix food, put spoon, take spoon, mix rice, put spoon ###\nclose door, touch car, hold hose, put hose, touch hand, pull wire, take hose, hold vacuum => pull vacuum, put vacuum, turn vacuum, clean floor, put hand, clean vacuum, clean cabinet, clean car, put chair, clean floor, take rod, attach pipe, clean floor, turn vacuum, take vacuum, move pipe, put vacuum, open door, move pipe, turn vacuum ###\ntake plier, press shoe, put plier, give shoe, carry shoe, take needle, sew shoe, put scraper => take plier, press shoe, put plier, throw shoe, carry string, put string, adjust plier, carry cloth, put cloth, carry shoe, take awl, sew shoe, put money, take money, sew shoe, take money, put money, sew shoe, insert awl, sew shoe ###\ntake cloth, put cloth, put cloth, adjust cloth, put shirt, take shirt, adjust shirt, fold shirt => put shirt, take shirt, adjust shirt, fold cloth, put shirt, pack shirt, take shirt, put shirt, put cloth, take shirt, fold cloth, put shirt, touch bed, take cloth, move cloth, take cloth, put cloth, touch rail, take cloth, hold cloth ###\nmove calculator, put calculator, turn book, move calculator, take book, put book, adjust book, draw book => write book, turn book, write book, adjust book, adjust book, turn book, adjust book, write book, adjust book, mark book, turn book, mark book, adjust book, adjust book, mark book, put book, adjust book, turn book, adjust book, turn book ###\nmove ladder, climb ladder, peel wire, move wire, adjust plier, cut wire, attach wire, attach wire => adjust plier, attach wire, pull wire, hold wire, adjust wire, hold wire, cut wire, attach wire, attach wire, adjust wire, peel wire, attach wire, attach wire, remove screw, attach wire, screw wire, move wire, put wire, hold wire, attach wire ###\ntake nut, take nut, move nut, take wrench, move wrench, insert nut, put nut, take screw => tighten pipe, take screw, tighten pipe, hold wrench, put wrench, hold pipe, take wrench, tighten screw, move nut, tighten screw, put wrench, remove screw, hold screw, hold screw, hold pipe, hold screw, insert screw, hold pipe, take screw, tighten screw ###\nquestion:\nput shoe, take shoe, put shoe, take shoe, put shoe, take shoe, arrange shoe, put shoe =>"
input_ids = tokenizer(prompt, return_tensors="pt").input_ids.to(model.device)

generated_ids = model.generate(input_ids, max_length=4096)
print(tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0])
