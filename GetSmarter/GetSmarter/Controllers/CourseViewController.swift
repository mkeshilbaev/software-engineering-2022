//
//  CourseViewController.swift
//  GetSmarter
//
//  Created by Madi Keshilbayev on 13.05.2022.
//

import UIKit

class CourseViewController: UIViewController {

//    @IBOutlet var imageView: UIImageView!
//    @IBOutlet var nameLabel: UILabel!
//    @IBOutlet var authorLabel: UILabel!
//    @IBOutlet var button: UIButton!
//    @IBOutlet var scrollView: UIScrollView!
//    @IBOutlet var descriptionLabel: UILabel!
//
//    private var book: Book?
//    private let dataProvider = DataProvider()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
//        button.layer.cornerRadius = 20
//        button.alpha = 0
//        button.layer.borderColor = UIColor.white.cgColor
//        UIView.animate(withDuration: 1.3,
//                       delay: 0.7,
//                       options: .curveEaseInOut,
//                       animations: {
//                        self.button.alpha = 1
//        })
//
//        setViews()
//
//        navigationItem.rightBarButtonItem = UIBarButtonItem(image: UIImage(systemName: "heart"), style: .plain, target: self, action: #selector(didTapAddToFavorite))
//
//        guard let book = book else { return }
//        if book.isFavorite == false{
//            self.navigationItem.rightBarButtonItem?.tintColor = .systemBlue
//        }else{
//            self.navigationItem.rightBarButtonItem?.tintColor = .red
//        }
        
    }
    
//    override func viewWillAppear(_ animated: Bool) {
//        super.viewWillAppear(animated)
//
//        guard let book = book else { return }
//        if book.isFavorite == false{
//            self.navigationItem.rightBarButtonItem?.tintColor = .systemBlue
//        }else{
//            self.navigationItem.rightBarButtonItem?.tintColor = .red
//        }
//    }
//
//    @IBAction func didTapPlay(_ sender: Any) {
//        let storyboard = UIStoryboard(name: "Main", bundle: nil)
//        guard let viewController = storyboard.instantiateViewController(identifier: "PlayerViewController") as? PlayerViewController, let book = book else { return }
//        viewController.configure(book: book)
//        navigationController?.pushViewController(viewController, animated: true)
//    }
//
//    @objc
//    func didTapAddToFavorite() {
//        guard var book = book else { return }
//        book.isFavorite.toggle()
//        self.book = book
//        dataProvider.addToFavorite(book: book)
//
//        if self.navigationItem.rightBarButtonItem?.tintColor == .systemBlue{
//            self.navigationItem.rightBarButtonItem?.tintColor = .red
//        }else{
//            self.navigationItem.rightBarButtonItem?.tintColor = .blue
//        }
//    }
//
//    func configure(book: Book) {
//        self.book = book
//    }
//
//    func setViews() {
//        guard let book = book else { return }
//        URLSession.shared.dataTask(with: URL(string: book.pictureUrl)!) { (data, response, error) in
//            if error != nil {
//                return
//            }
//            if let data = data {
//                DispatchQueue.main.async {
//                    self.imageView.image = UIImage(data: data)
//                }
//            }
//        }.resume()
//        nameLabel.text = book.title
//        authorLabel.text = book.author
//        descriptionLabel.text = book.description
//    }
    
}
