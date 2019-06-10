{
    "targets": [
    {
        'target_name': 'sword',
        'type': 'none',
        'actions': [
            {
                'action_name': 'build_sword',
                'message': 'Building sword library...',
                'inputs': [],
                'outputs': ['sword_build/libsword.a'],
                'action': ['./build_sword.sh'],
            },
        ]
    },
    {
        "target_name": "node_sword_interface",
        "cflags!": [ "-fno-exceptions" ],
        "cflags_cc!": [ "-fno-exceptions -std=c++11 -pthread" ],
        "sources": [
            "file_system_helper.cpp",
            "sword_facade.cpp",
            "node_sword_interface.cpp",
            "binding.cpp"
        ],
		"conditions":[
			["OS=='linux'", {
			    'include_dirs': [
					"<!@(node -p \"require('node-addon-api').include\")",
					"sword/include"
				],
				"libraries": [
					'<(module_root_dir)/sword_build/libsword.a',
					'<!@(pkg-config --libs libcurl)',
                    '<!@(icu-config --ldflags)'
				],
				"dependencies": [
					 "<!(node -p \"require('node-addon-api').gyp\")",
					 'sword'
				 ]
			}],
			["OS=='mac'", {
			    'include_dirs': [
					"<!@(node -p \"require('node-addon-api').include\")",
					"sword/include"
				],
				"libraries": [
					'<(module_root_dir)/sword_build/libsword.a',
					'<!@(pkg-config --libs libcurl)'
				],
				"dependencies": [
					 "<!(node -p \"require('node-addon-api').gyp\")",
					 'sword'
				 ]
			}],
			["OS=='win'", {
			    'include_dirs': [
					"<!@(node -p \"require('node-addon-api').include\")",
					"F:\dev\sword-dep\sword\include"
				],
				"libraries": [
                    '-lF:/dev/sword-libs/libsword.lib',
					'-lF:/dev/sword-libs/icuuc.lib',
					'-lF:/dev/sword-libs/icuin.lib',
					'-lF:/dev/sword-libs/icudt.lib',
					'-lF:/dev/sword-libs/libbz2.lib',
					'-lF:/dev/sword-libs/liblzma.lib',
					'-lF:/dev/sword-libs/libcurl_imp.lib',
					'-lWldap32.lib',
					'-lWs2_32.lib',
					'-lcrypt32.lib',
					'-lNormaliz.lib'
				],
				'defines': [ '_HAS_EXCEPTIONS=1' ]
			}]
        ], 
        'dependencies': [
            "<!(node -p \"require('node-addon-api').gyp\")"
        ],
        'defines': [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
    }]
}
