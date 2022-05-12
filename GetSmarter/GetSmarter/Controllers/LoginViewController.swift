//
//  LoginViewController.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 13.05.2022.
//

import UIKit
import Firebase
import FirebaseAuth

class LoginViewController: UIViewController {
    
    var current_user: User?
    @IBOutlet weak var email_field: UITextField!
    @IBOutlet weak var password_field: UITextField!
    @IBOutlet var loginButton: UIButton!
    @IBOutlet weak var indicator: UIActivityIndicatorView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        current_user = Auth.auth().currentUser
        
        loginButton.layer.cornerRadius = 20
        loginButton.alpha = 0
        loginButton.layer.borderColor = UIColor.white.cgColor
        UIView.animate(withDuration: 1.3,
                       delay: 0.7,
                       options: .curveEaseInOut,
                       animations: {
                        self.loginButton.alpha = 1

        })
        
        email_field.layer.cornerRadius = 20
        email_field.layer.transform = CATransform3DTranslate(CATransform3DIdentity, -500, 0, 0)
        UIView.animate(withDuration: 0.9,
                       delay: 0.4,
                       options: .curveEaseInOut,
                       animations: {
                        self.email_field.layer.transform = CATransform3DIdentity
        })
        
        password_field.layer.cornerRadius = 20
        password_field.layer.transform = CATransform3DTranslate(CATransform3DIdentity, 500, 0, 0)
        UIView.animate(withDuration: 0.9,
                       delay: 0.4,
                       options: .curveEaseInOut,
                       animations: {
                        self.password_field.layer.transform = CATransform3DIdentity
        })
    }
    
    override func viewDidAppear(_ animated: Bool){
        current_user = Auth.auth().currentUser
        if current_user != nil && current_user!.isEmailVerified{
            gotoMainPage()
        }
    }
    
    @IBAction func login_clicked(_ sender: UIButton) {
        let email = email_field.text?.trimmingCharacters(in: .whitespacesAndNewlines)
        let password = password_field.text?.trimmingCharacters(in: .whitespacesAndNewlines)
        
        indicator.startAnimating()
        Auth.auth().signIn(withEmail: email!, password: password!) { [weak self]
            (result, error) in
            self?.indicator.stopAnimating()
            if error == nil {
                if Auth.auth().currentUser!.isEmailVerified{
                    //go to main page
                    self?.gotoMainPage()
                } else{
                    self?.showMessage(title: "Warning", message: "Email was not verified!")
                }
            }else{
                self?.showMessage(title: "Error", message: "Invalid username/password!")
            }
          
        }
    }
    
    func showMessage(title: String, message: String) {
        // create the alert
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        
        //add and action (button)
        let ok = UIAlertAction(title: "OK", style: .default){ (UIAlertAction) in
        }
        alert.addAction(ok)
        
        //show the alert
        self.present(alert, animated: true, completion: nil)
    }
    
    func gotoMainPage(){
        let storyboard = UIStoryboard(name: "Main", bundle: Bundle.main)
        if let mainPage = storyboard.instantiateViewController(identifier: "MainTabBarController") as? UITabBarController{
            
            mainPage.modalPresentationStyle = .fullScreen
            present(mainPage, animated: true, completion: nil)
        }
    }

}
