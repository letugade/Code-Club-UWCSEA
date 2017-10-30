//
//  ViewController.swift
//  Calculator
//
//  Created by Vaishant Kameswaran on 10/10/17.
//  Copyright © 2017 VaiRox. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {
    var n1 : IntMax = 0
    @IBOutlet var btn1: NSButton!
    @IBOutlet var txtDisplay: NSTextField!
    @IBOutlet var btnClear: NSButton!
    @IBOutlet var btnAdd: NSButton!
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

    override var representedObject: Any? {
        didSet {
        // Update the view, if already loaded.
        }
    }
    @IBAction func pushBtn1(_ sender: NSButton) {
        txtDisplay.stringValue += "1"
    }
    @IBAction func btnAddPushed(_ sender: Any) {
        n1 = IntMax(txtDisplay.doubleValue)
        txtDisplay.stringValue = ""
    }
    @IBAction func btnClearPushed(_ sender: Any) {
        txtDisplay.stringValue = ""
    }

}

