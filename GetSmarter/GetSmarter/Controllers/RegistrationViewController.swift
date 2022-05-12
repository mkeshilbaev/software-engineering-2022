//
//  RegistrationViewController.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 12.05.2022.
//


import UIKit
import Firebase
import FirebaseAuth
import FirebaseStorage

class RegistrationViewController: UIViewController {
    
    @IBOutlet weak var name: UITextField!
    @IBOutlet weak var surname: UITextField!
    @IBOutlet weak var birth_date: UITextField!
    @IBOutlet weak var email_field: UITextField!
    @IBOutlet weak var password_field: UITextField!
    @IBOutlet weak var confirm_password_field: UITextField!
    @IBOutlet var registerButton: UIButton!
    @IBOutlet weak var indicator: UIActivityIndicatorView!
    let storageRef = Storage.storage().reference()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        name.layer.cornerRadius = 20
        name.layer.transform = CATransform3DTranslate(CATransform3DIdentity, -500, 0, 0)
        UIView.animate(withDuration: 0.9,
                       delay: 0.4,
                       options: .curveEaseInOut,
                       animations: {
                        self.name.layer.transform = CATransform3DIdentity
        })
        
        surname.layer.cornerRadius = 20
        surname.layer.transform = CATransform3DTranslate(CATransform3DIdentity, 500, 0, 0)
        UIView.animate(withDuration: 0.9,
                       delay: 0.4,
                       options: .curveEaseInOut,
                       animations: {
                        self.surname.layer.transform = CATransform3DIdentity
        })
        birth_date.layer.cornerRadius = 20
        birth_date.layer.transform = CATransform3DTranslate(CATransform3DIdentity, -500, 0, 0)
        UIView.animate(withDuration: 0.9,
                       delay: 0.4,
                       options: .curveEaseInOut,
                       animations: {
                        self.birth_date.layer.transform = CATransform3DIdentity
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
        confirm_password_field.layer.cornerRadius = 20
        confirm_password_field.layer.transform = CATransform3DTranslate(CATransform3DIdentity, 500, 0, 0)
        UIView.animate(withDuration: 0.9,
                       delay: 0.4,
                       options: .curveEaseInOut,
                       animations: {
                        self.confirm_password_field.layer.transform = CATransform3DIdentity
        })
        registerButton.layer.cornerRadius = 20
        registerButton.alpha = 0
        registerButton.layer.borderColor = UIColor.white.cgColor
        UIView.animate(withDuration: 1.3,
                       delay: 0.7,
                       options: .curveEaseInOut,
                       animations: {
                        self.registerButton.alpha = 1
        })
    }

    @IBAction func register_clicked(_ sender: UIButton) {
        guard let name = name.text else { return }
        guard let surname = surname.text else { return }
        guard let email = email_field.text else { return }
        guard let password = password_field.text else { return }
        guard let birth_date = birth_date.text else { return }
                
        if email != "" && password != ""{
            indicator.startAnimating()
            Auth.auth().createUser(withEmail: email, password: password) { [weak self] (result, error) in
                self?.indicator.stopAnimating()
                Auth.auth().currentUser?.sendEmailVerification(completion: nil)
                if error == nil{
                    Database.database().reference().child("users").child((result?.user.uid)!).setValue(["name": name, "surname": surname, "email": email, "birth_date": birth_date])
                    self?.showMessage(title: "Success", message: "Please verify your email")
                }else{
                    self?.showMessage(title: "Error", message: "Couldn't sign up the user!")
                }
            }
        }
    }
    
    func showMessage(title: String, message: String) {
        // create the alert
        let alert = UIAlertController(title: title, message: message, preferredStyle: .alert)
        //add and action (button)
        let ok = UIAlertAction(title: "OK", style: .default){ (UIAlertAction) in
            if title != "Error"{
                self.dismiss(animated: true, completion: nil)
            }
        }
        alert.addAction(ok)
        //show the alert
        self.present(alert, animated: true, completion: nil)
    }
}
