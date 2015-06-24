#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from ast import literal_eval

import sys
import re

from stroke import Stroke
import stroke

import os.path

import argparse
parser = argparse.ArgumentParser(description='study of log from ABC writer')
parser.add_argument('session', action="store",
                help='pre-test_post-test analysis')


optimal_5 = "[0.384057971014 0.261567464485 0.197667629695 0.0816660085652 -0.00440566609228 -0.140472676258 -0.256491462802 -0.338229883296 -0.382085487718 -0.413521090541 -0.413038791269 -0.416852974564 -0.420292715375 -0.420952599295 -0.412451838673 -0.420285420695 -0.428258583881 -0.434183083379 -0.442016586753 -0.442028974646 -0.442042581755 -0.434874109522 -0.434786078475 -0.420289855072 -0.377177061268 -0.348832691991 -0.291577806642 -0.254559216915 -0.172181549423 -0.105270602782 -0.0403056142805 0.0117410496839 0.0702649407217 0.117015203781 0.159713997184 0.206322013387 0.263973865091 0.30986560194 0.350400167764 0.387222072047 0.422061663579 0.443227255209 0.464479438812 0.485345200072 0.492747037646 0.492749510342 0.5 0.492697041196 0.486207150786 0.463432582702 0.448889052645 0.423030378814 0.405872095099 0.359220307334 0.309229885035 0.252660132608 0.202630777478 0.148939216217 0.0474020470811 -0.0102019550865 -0.0756732227515 -0.15100759168 -0.220039666369 -0.262536071943 -0.328317137166 -0.37047801217 -0.42196661685 -0.463476086258 -0.478361672553 -0.5 -0.760812885288 -0.760812885288 -0.760812885288 -0.760812885288 -0.760812884914 -0.760813193689 -0.760569410568 -0.76064966956 -0.761591995733 -0.750426566518 -0.706004483632 -0.670061295046 -0.626167738735 -0.590804732411 -0.540996823739 -0.473249427541 -0.408888761791 -0.336911619956 -0.257075397024 -0.208837548122 -0.172908506258 -0.128950296999 -0.0865850603221 -0.0579143345632 -0.0582550576214 -0.0651440274355 -0.0723563293764 -0.0724071806674 -0.0724104757739 -0.0668064786106 -0.0651585252653 -0.0649565859506 -0.0533215255616 -0.0514341862059 -0.0434773991235 -0.0255062918735 0.0111018342626 0.0317652884402 0.0511906315574 0.0804522584393 0.094235381725 0.10921646595 0.132584146751 0.174684833436 0.218095478309 0.268390017243 0.31889725964 0.354800925309 0.397668489941 0.462208572201 0.513195122134 0.562288998383 0.599754700718 0.655206019842 0.701549779901 0.722662160754 0.744024752732 0.753488785838 0.757116044753 0.761591995733 0.753729297504 0.736669429131 0.709311762987 0.694124562448 0.674334335046 0.650838258014 0.607224624956 0.55737555518 0.52131242334 0.478317549495]"

optimal_8 = "[-0.0243213471502 0.0904459346802 0.191879977758 0.247243028688 0.312891090082 0.368296981283 0.412849361758 0.461527515922 0.490121537675 0.5 0.489490843252 0.453843360683 0.379630108469 0.303186796174 0.189037555525 0.0791228466465 -0.00776954936266 -0.0805627647689 -0.166169011807 -0.238016595293 -0.319994071421 -0.359383062304 -0.423849299916 -0.452531343391 -0.462020679872 -0.462736824738 -0.442512346492 -0.423525114127 -0.395364769417 -0.350865228925 -0.239046322262 -0.128424743986 -0.028370511862 0.0736934132185 0.134984725525 0.208510014058 0.264964236436 0.317522563737 0.336346085375 0.316846967057 0.284559505165 0.259770825994 0.21768485669 0.153803068304 0.125789464008 0.0727135855481 0.0168916929503 -0.0287440210235 -0.0976567128322 -0.157609520968 -0.213648261006 -0.250113262377 -0.302327265797 -0.381254479447 -0.434108906693 -0.470637858234 -0.489273797899 -0.5 -0.489550546621 -0.480976641699 -0.462761050442 -0.443353281481 -0.41300996464 -0.375293124575 -0.339097749419 -0.294286429658 -0.226592759017 -0.183043755797 -0.173437914232 -0.127793658783 -1.0562031225 -1.04820360574 -1.02836322248 -1.00095349005 -0.980599372324 -0.956094845959 -0.912745691564 -0.857278166152 -0.792776256007 -0.701462207942 -0.565969457 -0.448209749574 -0.306196128675 -0.203167676581 -0.0863271025033 -0.032994443288 0.0333441306285 0.0993569872153 0.15461469303 0.236364888641 0.318239019832 0.376858546444 0.472278036731 0.572313201034 0.683344750067 0.784175984946 0.855493567219 0.93888438073 0.99590142047 1.02147806244 1.06707739146 1.08487094069 1.08597731816 1.07613883833 1.06473326067 1.02900967065 0.972948760234 0.895052363327 0.823693087116 0.713764533598 0.553867498814 0.439134254025 0.330490462435 0.212379669088 0.166851351856 0.0788993968472 0.00747744375169 -0.0385102414128 -0.0838168546241 -0.129655801401 -0.195230035259 -0.240090048148 -0.30575238173 -0.380587637759 -0.445232068228 -0.528384536461 -0.611984487128 -0.672269078703 -0.765406796366 -0.835994740504 -0.881867452356 -0.937868708212 -0.962912873264 -0.989929644196 -1.00586739405 -1.03404106579 -1.04845452808 -1.05715979346 -1.08597731816 -1.07607518728]"

optimal_h = "[-0.465644654167 -0.406814716731 -0.317143484748 -0.25655215878 -0.184507813269 -0.118441201034 -0.0553834723074 -0.00932181178393 0.0194183811841 0.0234560320212 0.0229741558399 0.0198558402606 0.00518230513048 -0.00561355548688 -0.023476604695 -0.0456369309396 -0.0609669212641 -0.0783039569565 -0.0958308290006 -0.107504694821 -0.122015898631 -0.136546908227 -0.141697091876 -0.152690297875 -0.160242702095 -0.167886986693 -0.175414043936 -0.181501300613 -0.186817315464 -0.202738509777 -0.205912789304 -0.210021834416 -0.213345106856 -0.218603215225 -0.221366744246 -0.221622582653 -0.222464888308 -0.217520769696 -0.213860829694 -0.209908890338 -0.209877010992 -0.199882227334 -0.177189355294 -0.159481907181 -0.133505492852 -0.115017680319 -0.0931300084864 -0.0707479700553 -0.0477553518672 -0.0226805478612 -0.000729895945079 0.0172570655237 0.0322046529855 0.0461909624767 0.0534823572588 0.0685681214828 0.086925268026 0.0966687412317 0.111186442505 0.137582010585 0.155940148501 0.18842436246 0.22434651268 0.276803976787 0.332196893204 0.372666728477 0.410512178739 0.442746638623 0.454999833182 0.465644654167 0.206077769288 0.179962153339 0.117240601299 0.0696779201395 0.00106180971476 -0.0685579308667 -0.150194344883 -0.220277212671 -0.281668917342 -0.333703471297 -0.400495776588 -0.449510260463 -0.477053243392 -0.491956223732 -0.5 -0.496146846969 -0.481924725827 -0.463591255741 -0.436289465091 -0.407659440751 -0.35158958548 -0.299581285651 -0.251533617647 -0.195213985023 -0.128588095061 -0.0693932595753 -0.00639604632691 0.0438122242381 0.0952219824064 0.164920079353 0.224070719923 0.278726506941 0.337625369441 0.403524200395 0.454650607261 0.480701551145 0.485719172567 0.46424038153 0.433112014726 0.404273230851 0.371250460824 0.323485169112 0.267361860776 0.222522910558 0.198115385606 0.183044438119 0.167694094733 0.167910095626 0.167967785496 0.171848896587 0.190358226595 0.220416453598 0.250870059972 0.284195782296 0.3245905463 0.364946574833 0.401887892924 0.441108532437 0.469566505624 0.492441707905 0.49993204743 0.5 0.492162200469 0.475168963272 0.423450794606 0.369193965061 0.314342686513 0.261903197016 0.231693565608 0.213711288209]"

ref_shape5 = literal_eval(optimal_5.replace(' ',', '))
ref_shape5 = np.reshape(ref_shape5, (-1, 1))
ref_stroke5 = Stroke()
ref_stroke5.stroke_from_xxyy(np.reshape(ref_shape5,len(ref_shape5)))
ref_stroke5.uniformize()
ref_stroke5.normalize()

ref_shape8 = literal_eval(optimal_8.replace(' ',', '))
ref_shape8 = np.reshape(ref_shape8, (-1, 1))
ref_stroke8 = Stroke()
ref_stroke8.stroke_from_xxyy(np.reshape(ref_shape8,len(ref_shape8)))
ref_stroke8.uniformize()
ref_stroke8.normalize()

ref_shapeh = literal_eval(optimal_h.replace(' ',', '))
ref_shapeh = np.reshape(ref_shapeh, (-1, 1))
ref_strokeh = Stroke()
ref_strokeh.stroke_from_xxyy(np.reshape(ref_shapeh,len(ref_shapeh)))
ref_strokeh.uniformize()
ref_strokeh.normalize()

results = {}

letters = {"num5-outset","num5-nooutset","num5-wire","num8-outset","num8-nooutset","num8-wire","h-outset","h-nooutset","h-wire"}
sessions = ["22_05_pre","22_05_post","12_06_pre","12_06_post","19_06_post"]

def showShape(shape ):
    plt.figure(1)
    plt.clf()
    ShapeModeler.normaliseAndShowShape(shape)

if __name__ == "__main__":

    with open(sys.argv[1], 'r') as log:

        indice = -1
        current_letter = ""
        is_stroke = False

        num_out = 0
        num_strokes = 0
        stroke_x = []
        stroke_y = []

        for line in log.readlines():
            if "Starting now" in line:
                indice += 1
                if indice>0:
                    result = {}
                    result["num_out"] = num_out
                    result["num_strokes"] = num_strokes
                    result["stroke_x"] = stroke_x
                    result["stroke_y"] = stroke_y
                    #results[sessions[indice-1]] = {}
                    results[sessions[indice-1]][current_letter] = result
                    num_out = 0
                    num_strokes = 0
                    stroke_x = []
                    stroke_y = []
                results[sessions[indice]] = {}

            elif "State:" in line:
                if current_letter:
                    result = {}
                    result["num_out"] = num_out
                    result["num_strokes"] = num_strokes
                    result["stroke_x"] = stroke_x
                    result["stroke_y"] = stroke_y
                    #results[sessions[indice]] = {}
                    results[sessions[indice]][current_letter] = result
                    num_out = 0
                    num_strokes = 0
                    stroke_x = []
                    stroke_y = []

                for letter in letters:
                    if letter in line:
                        current_letter = letter
                        #print letter

            elif "Clearing" in line:
                num_out = 0
                num_strokes = 0
                stroke_x = []
                stroke_y = []

            elif "Touch outside" in line:
                num_out += 1

            else :
                num_strokes += 1
                #print line
                #print line.slit(' ')
                trajectory = line.split(' ')[-1]
                #print trajectory
                for (x,y) in literal_eval(trajectory):
                    stroke_x.append(x)
                    stroke_y.append(y)

    # last adds :
    result = {}
    result["num_out"] = num_out
    result["num_strokes"] = num_strokes
    result["stroke_x"] = stroke_x
    result["stroke_y"] = stroke_y
    #results[sessions[indice]] = {}
    results[sessions[indice]][current_letter] = result

    # plot 5_outset
    #print results

    outs = np.zeros(len(sessions))
    cuts = np.zeros(len(sessions))
    dists = np.zeros(len(sessions))
    num = np.zeros(len(sessions))
    strokes5 = []
    strokes8 = []
    strokesh = []
    for letter in letters: #{"num8-outset","num8-nooutset","num8-wire"}:
        letter_outs = []
        letter_cuts = []
        letter_dist = []
        occurences = []
        for session in sessions:
            stroke_x = results[session][letter]["stroke_x"]
            stroke_y = results[session][letter]["stroke_y"]
            if len(stroke_x)>0:
                draw = Stroke(np.array(stroke_x),-np.array(stroke_y))
                draw.downsampleShape(70)
                draw.uniformize()
                draw.normalize()
                if letter in {"num5-outset","num5-nooutset","num5-wire"}:
                    _,_,dist,_,_,_ = stroke.best_aligment(draw,ref_stroke5)
                    strokes5.append(draw)
                if letter in {"num8-outset","num8-nooutset","num8-wire"}:
                     _,_,dist,_,_,_ = stroke.best_aligment(draw,ref_stroke8)
                     strokes8.append(draw)
                if letter in {"h-outset","h-nooutset","h-wire"}:
                    _,_,dist,_,_,_ = stroke.best_aligment(draw,ref_strokeh)
                    strokesh.append(draw)
                letter_dist.append(dist)
                occurences.append(1)
            else:
                letter_dist.append(0)
                occurences.append(0)
            letter_outs.append(results[session][letter]["num_out"])
            letter_cuts.append(results[session][letter]["num_strokes"])

        outs += np.array(letter_outs)
        cuts += np.array(letter_cuts)
        dists += np.array(letter_dist)
        num += np.array(occurences)

    plt.figure()

    plt.subplot(3,1,1)
    plt.plot(range(len(outs)),outs/num)
    plt.plot(range(len(outs)),outs/num,'rs')
    plt.xticks(range(len(outs)),sessions)
    plt.ylabel('outs')

    plt.subplot(3,1,2)
    plt.plot(range(len(outs)),cuts/num)
    plt.plot(range(len(outs)),cuts/num,'rs')
    plt.xticks(range(len(outs)),sessions)
    plt.ylabel('cuts')

    plt.subplot(3,1,3)
    plt.plot(range(len(outs)),dists/num)
    plt.plot(range(len(outs)),dists/num,'rs')
    plt.xticks(range(len(outs)),sessions)
    plt.ylabel('distances')


    plt.figure()
    stroke.plot_list(strokes5)
    plt.figure()
    stroke.plot_list(strokes8)
    plt.figure()
    stroke.plot_list(strokesh)

    plt.show()
